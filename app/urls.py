from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("agenda/", views.agenda, name="agenda"),
    path("projections", views.projections, name="projections")



]