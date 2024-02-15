from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.urls import reverse
from app.models import Movie, Hall, Projection, Seat, Ticket
import datetime

def create_movie(name, duration, genre, img_url, price):
    return Movie.objects.create(name=name, duration=duration, genre=genre, img_url=img_url, price=price)

def create_hall(name, type):
     return Hall.objects.create(name=name, type=type)

def create_Projection(self, param):
        prj = Projection.objects.create(start_date=param["start_date"], time=param["time"], movie=param["movie"], Hall=param['hall'])



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