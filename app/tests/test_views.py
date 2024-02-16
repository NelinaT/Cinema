from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.urls import reverse
from app.models import Movie, Hall, Projection, Seat, Ticket
import datetime
from django.contrib.auth.models import Group


def create_movie(name, duration, genre, img_url, price):
    return Movie.objects.create(name=name, duration=duration, genre=genre, img_url=img_url, price=price)

def create_hall(name, type):
     return Hall.objects.create(name=name, type=type)

def create_Projection(param):
    return  Projection.objects.create(start_date=param["start_date"], time=param["time"], movie=param["movie"], Hall=param['hall'])



class indexTest(TestCase):
    # movie = create_movie("IT",130,"horror","...", 10)
    # movie2 = create_movie("After",130,"romance","...", 10)

    def test_no_movies(self):

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No movies are available.")
        self.assertQuerySetEqual(response.context["movies"], [])


    def test_one_movie(self):
        movie = create_movie("IT",130,"horror","...", 10)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["movies"],
            [movie],
        )

    def test_many_movies(self):
        movie = create_movie("IT",130,"horror","...", 10)
        movie2 = create_movie("After",130,"Romance","...", 10)
        movie3= create_movie("Bad boys",130,"Comedy","...", 10)

        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["movies"],
            [movie3,movie2, movie],
            ordered=False
        )
    
class agendaTest(TestCase):

    
    def test_one_prj(self):
        self.group = Group(name="sales")
        self.group.save()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.groups.add(self.group)
        login = self.client.login(username='testuser', password='12345')
        
        hall= create_hall("vip","vip")
        movie = create_movie("IT",130,"horror","...", 10)
        param={
            "start_date":datetime.date(2024, 2, 19),
            "time": datetime.time(17,30),
            "movie": movie,
            "hall":hall
            }
        prj=create_Projection(param)
        url = reverse("agenda")
        response = self.client.get(url)

        self.assertQuerySetEqual(
            response.context["projections"],
            [prj],
        )

        self.assertQuerySetEqual(
            response.context["dates"],
            [prj.start_date],
        )

        self.assertTrue(
            response.context["is_sales_user"]
        )

def test_many_prj(self):
        self.group = Group(name="sales")
        self.group.save()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.groups.add(self.group)
        login = self.client.login(username='testuser', password='12345')
        
        hall= create_hall("vip","vip")
        movie = create_movie("IT",130,"horror","...", 10)
        param={
            "start_date":datetime.date(2024, 2, 19),
            "time": datetime.time(17,30),
            "movie": movie,
            "hall":hall
            }
        param2={
            "start_date":datetime.date(2024, 2, 19),
            "time": datetime.time(22,30),
            "movie": movie,
            "hall":hall
            }
        prj = create_Projection(param)
        prj2 = create_Projection(param2)

        url = reverse("agenda")
        response = self.client.get(url)

        self.assertQuerySetEqual(
            response.context["projections"],
            [prj, prj2],
        )

        self.assertQuerySetEqual(
            response.context["dates"],
            [prj.start_date],
        )

        self.assertTrue(
            response.context["is_sales_user"]
        )