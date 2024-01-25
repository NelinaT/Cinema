from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Movie, Hall, Projection
from  django.contrib.auth.models import User


def index(request):
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

                return redirect("agenda")
    
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
    return render (
        request,
        "customer/agenda.html"
    )

@login_required(login_url="../login")
def projections(request):
    mv=Movie.objects.get(pk=request.GET.get('id',''))
    print(mv.toStr())
    prj = Projection.objects.all().filter(movie=mv).order_by('start_date')
    return render(
        request,
        "common/projections.html",
        context={
            "movie": mv,
            "projections": prj
        }
    )