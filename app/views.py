from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Movie, Hall, Projection
from  django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime


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
def hall(request):
    prj=Projection.objects.get(pk=request.GET.get('id',''))
    print(prj.Hall.type)
    return render(request, 
                  "common/hall.html",
                  context={
                      "hall_id": f"app/{prj.id}.svg",
                      "hall_type": prj.Hall.type
                  }
                )

def is_sales(user):
    return user.groups.filter(name='sales').exists()