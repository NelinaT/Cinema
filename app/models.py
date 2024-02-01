from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.core.exceptions import ValidationError
from . hall_builder import generate_svg
from  django.contrib.auth.models import User


capacity_for_hall_types = {
    "vip": {
        "rows": 6,
        "cols": 8
    },
    "std": {
        "rows": 5,
        "cols": 10
    },
    "big": {
        "rows": 10,
        "cols": 10
    },
}

row_names = ["A","B", "C","D","E","F","G","H","I","J"]

class Hall(models.Model):
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=[("vip", "VIP"),("std", "standart"),("big", "big")])
    def __str__(self):
        return self.name
    
    def toStr(self):
        return "{\n\tid: " + str(self.pk) + "\n\tname: "+ self.name + "\n\ttype: "+ self.type +"\n}"

    def save(self, *args, **kwargs):
        is_creating_new_row_in_db = self._state.adding
        super(Hall, self).save(*args, **kwargs)
        if is_creating_new_row_in_db:
            for i in range(capacity_for_hall_types[self.type]['rows']):
                for j in range(capacity_for_hall_types[self.type]['cols']):
                    Seat(hall=self, row=row_names[i], col=j+1).save()
            


class Seat(models.Model):
    hall = models.ForeignKey(Hall,on_delete=models.CASCADE)
    row = models.CharField(max_length=1)
    col = models.IntegerField()
    is_available = models.BooleanField(default = True)
    
    def __str__(self):
        return self.hall.name + " - row: " + str(self.row) + " col: " + str(self.col)
    
    

class Movie(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    img_url = models.CharField(max_length = 100, default='')
    price = models.IntegerField(default = 10)
    def __str__(self):
        return self.name
    def toStr(self):
        return "{\n\tid: " + str(self.pk) + "\n\tname: "+ self.name +  "\n\tduration: "+ self.duration.__str__() + "\n\tgenre: "+ self.genre +"\n\timg_url: "+ self.img_url +"\n}"

class Projection(models.Model):
    start_date = models.DateField(default=now)
    time = models.TimeField(default=now)
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True)
    Hall = models.ForeignKey(Hall,on_delete=models.SET_NULL,null=True)

    @property
    def price(self):
        if self.Hall and self.movie:
            if self.Hall.type == "vip":
                return self.movie.price + 5
            if self.Hall.type == "std":
                return self.movie.price + 2
            if self.Hall.type == "big":
                return self.movie.price
        return 0     

    @property
    def hall_capacity(self):
        if self.Hall.type == "vip":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,550, 6, 8)
        if self.Hall.type == "std":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,600, 6, 10)
        if self.Hall.type == "big":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,1000, 10, 10)




    def __str__(self):
        return self.movie.name
    
    @staticmethod
    def time_in_range(start, end, current):
        return start <= current <= end
    
    def clean(self):
        all_projections_per_hall = Projection.objects.all().filter(Hall = self.Hall).filter(start_date = self.start_date)

        for projection in all_projections_per_hall:
            duration = projection.movie.duration
            start_time = projection.time
            end_time = timedelta(hours=start_time.hour ,minutes = start_time.minute) + timedelta(minutes = duration)  + timedelta(minutes=20)
            start_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
            new_time = timedelta(hours=self.time.hour, minutes=self.time.minute)
            if Projection.time_in_range(start_time , end_time, new_time):
                raise ValidationError("There is a projestion in this time")

    def save(self, *args, **kwargs):
        super(Projection, self).save(*args, **kwargs)
        self.hall_capacity
    

class Ticket(models.Model):
    is_empty = models.BooleanField(default = True)
    projection = models.ForeignKey(Projection,on_delete=models.SET_NULL,null=True)
    seat = models.ForeignKey(Seat,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

