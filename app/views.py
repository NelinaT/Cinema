from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Movie, Hall, Projection, Seat, Ticket
from  django.contrib.auth.models import User
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.template import RequestContext
from . utils import digitToChar, charToDigit
import json


def index(request):
    if is_sales(request.user):
        return redirect('agenda')
    Movies = Movie.objects.all()
    return render(
        request,
        "common/index.html",
        context={"movies": Movies}
    )

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form =LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)

                return redirect("index")
    
    context = {"loginform":form}
            
    return render(request, "registration/login.html", context=context)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm (request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, 'Something went wrong. Try again!')

    context = {"register_form": form}
    
    return render(request, "registration/register.html", context=context)


def logout(request):
    auth.logout(request)

    return redirect("../login")

@login_required(login_url="../login")
def agenda(request):
    prj = Projection.objects.all().order_by('start_date')
    dates = prj.values_list('start_date', flat=True).filter(start_date__gte=now().strftime('%Y-%m-%d')).distinct()

    if len(dates) > 0:
        selected_date = dates[0]
        if request.GET.get('date',''):
            selected_date = request.GET.get('date','')
        prj = prj.filter(start_date = selected_date).order_by("time")
        selected_date = prj.first().start_date
    return render (
    request,
    "salesAsistant/agenda.html",
    context={
        "selected_date":selected_date,
        "dates": dates,
        "projections": prj
    })

@login_required(login_url="../login")
def projections(request):
    print(request.user.groups)
    mv=Movie.objects.get(pk=request.GET.get('id',''))
    prj = Projection.objects.all().filter(movie=mv).filter(start_date__gte=now().strftime('%Y-%m-%d')).order_by('start_date')
   
    return render(
        request,
        "common/projections.html",
        context={
           
            "movie": mv,
            "projections": prj
        }
    )

@login_required(login_url="../login")
@requires_csrf_token
def hall(request):
    prj=Projection.objects.get(pk=request.GET.get('id',''))
    prj.hall_capacity()
    unavailable = Seat.objects.all().filter(hall = prj.Hall).filter(is_available = False)
    taken = Ticket.objects.all().filter(projection = prj).exclude(user__isnull = True)
    if prj.Hall.type == "big":
        row_count = 10
        row_range = range(10)
        col_range = range(10)
        starting_x = 199
        starting_y = 19
        starting_xx = 252
        starting_yy = 72
    elif prj.Hall.type == "std":
        row_count = 6
        row_range = range(6)
        col_range = range(10)
        starting_x = 199
        starting_y = 99
        starting_xx = 252
        starting_yy = 152
    else:
        row_count = 6
        row_range = range(6)
        col_range = range(8)
        starting_x = 199
        starting_y = 74
        starting_xx = 252
        starting_yy = 127
        
    def get_coords_list():
        result = []
        
        for i in row_range:
            for j in col_range:
                seat = {
                    "x": starting_x + (j*70),
                    "y": starting_y + (i*70),
                    "xx": starting_xx + (j*70),
                    "yy": starting_yy + (i*70),
                    "data_row": row_count -i,
                    "data_col": j+1
                }
                if is_available_seat(seat):
                    result.append(seat)

        return result

    def is_available_seat(seat):
        for t in taken:
            if t.seat.col == seat['data_col'] and t.seat.row == digitToChar(seat["data_row"]):
                return False
            
        for u in unavailable:
            if u.col == seat['data_col'] and u.row == digitToChar(seat["data_row"]):
                return False
            
        return True

    coords_list = get_coords_list()

    return render(request,
                  "common/hall.html",
                  context={
                      "hall_id": f"app/{prj.id}.svg",
                      "price": prj.price,
                      "coords" : coords_list,
                      "projection": prj
                    }
                )

@login_required(login_url="../login")
@requires_csrf_token
def payment(request):
    prj = Projection.objects.get(pk=request.POST.get("projId"))
    seats = json.loads(request.POST.get("seats"))
    print(seats)

    for s in seats:
        print(s["payment"])
        seat = Seat.objects.get(row = digitToChar(int(s["row"])), col=int(s["col"]), hall=prj.Hall)
        print(seat)
        payment_method =  s["payment"]
        ticket = Ticket(projection=prj,user=request.user,seat=seat, payment_method = payment_method)
        ticket.save()


    return render(
         request,
        "common/payment.html"
    )

def is_sales(user):
    return user.groups.filter(name='sales').exists()