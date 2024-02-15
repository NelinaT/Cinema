from django.test import TestCase
from django.db import models
from app.models import Movie, Hall, Projection, Seat, Ticket
import datetime
from django.core.exceptions import ValidationError

class ProjectionTests(TestCase):
    case_1 = {  
        "start_date":datetime.date(2024, 2, 19),
        "time": datetime.time(17,30),
        "movie": Movie.objects.get(pk=43),
        "hall": Hall.objects.get(pk=22)
    }

    case_2 = {  
        "start_date":datetime.date(2024, 2, 19),
        "time": datetime.time(17,30),
        "movie": Movie.objects.get(pk=44),
        "hall": Hall.objects.get(pk=23)
    }

    case_3 = {  
        "start_date": datetime.date(2024, 2, 19),
        "time": datetime.time(19,15),
        "movie": Movie.objects.get(pk=45),
        "hall": Hall.objects.get(pk=24)
    }
    
    case_4 = { 
        "start_date":datetime.date(2024, 2, 19),
        "time": datetime.time(17,30),
        "movie":Movie.objects.get(pk=46),
        "hall": case_1["hall"]
    }
    case_5 = { 
        "start_date":datetime.date(2024, 2, 19),
        "time": datetime.time(19,15),
        "movie":Movie.objects.get(pk=47),
        "hall": case_1["hall"]
    }
    case_6 = { 
        "start_date":datetime.date(2024, 2, 19),
        "time": datetime.time(17,15),
        "movie":Movie.objects.get(pk=48),
        "hall": case_1["hall"]
    }

    def create_Projection(self, param):
        prj = Projection.objects.create(start_date=param["start_date"], time=param["time"], movie=param["movie"], Hall=param['hall'])
        prj.movie.save()
        prj.Hall.save()
        # prj.save()
        return prj
    
    def test_price(self):
        prj = ProjectionTests.create_Projection(self,self.case_1)
        self.assertTrue(isinstance(prj, Projection))
        self.assertEqual(prj.price, 15)
        prj = ProjectionTests.create_Projection(self,self.case_2)
        self.assertEqual(prj.price, 10)
        prj = ProjectionTests.create_Projection(self,self.case_3)
        self.assertEqual(prj.price, 12)
    
    def test_no_projections_in_same_time_and_hall(self):

        # check creating a new projecion, when there are no projections
        prj = ProjectionTests.create_Projection(self,self.case_1)
        self.assertIsNot(ValidationError,prj.clean)

        # test if a projection can be created when there is a projection in this time and hall
        prj2 = ProjectionTests.create_Projection(self, self.case_4)
        self.assertRaises(ValidationError,prj2.clean)

        #test if a projection can be created when there is a projection in the same time but different hall
        prj3 = ProjectionTests.create_Projection(self, self.case_2)
        self.assertIsNot(ValidationError,prj3.clean)
        
        #test if a projection is in less than 20 minutes after the end of the previous
        prj4 = ProjectionTests.create_Projection(self, self.case_5)
        self.assertRaises(ValidationError,prj4.clean)

        #test if the end of the new projection is during abother projection
        prj5 = ProjectionTests.create_Projection(self, self.case_6)
        self.assertRaises(ValidationError,prj5.clean)
        

        # Projection.objects.all().delete()











   
