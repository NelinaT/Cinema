from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.core.exceptions import ValidationError
from . hall_builder import generate_svg
from  django.contrib.auth.models import User
import qrcode
from . utils import row_names


capacity_for_hall_types = {
    "vip": {
        "rows": 6,
        "cols": 8
    },
    "std": {
        "rows": 6,
        "cols": 10
    },
    "big": {
        "rows": 10,
        "cols": 10
    },
}


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
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.CharField(max_length=1)
    col = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
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
    hall = models.ForeignKey(Hall,on_delete=models.SET_NULL,null=True)

    @property
    def price(self):

        if self.hall and self.movie:
            if self.hall.type == "vip":
                return self.movie.price + 5
            if self.hall.type == "std":
                return self.movie.price + 2
            if self.hall.type == "big":
                return self.movie.price
        return 0     

    def hall_capacity(self):
        tickets = Ticket.objects.all().filter(projection=self)
        seats = Seat.objects.all().filter(hall=self.hall)

        if self.hall.type == "vip":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,550, seats, tickets, 8)
        if self.hall.type == "std":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,600, seats, tickets, 10)
        if self.hall.type == "big":
            return generate_svg(f"app/static/app/{self.id}.svg",1000,1000, seats, tickets, 10)

    def __str__(self):
        return f"{self.id} - {self.movie.name} "
    
    @staticmethod
    def time_in_range(start, end, current):
        return start <= current <= end
    
    def clean(self):
        all_projections_per_hall = Projection.objects.all().filter(hall = self.hall).filter(start_date = self.start_date)

        for projection in all_projections_per_hall:

            duration = projection.movie.duration
            start_time = projection.time
            end_time = timedelta(hours=start_time.hour ,minutes=start_time.minute) + timedelta(minutes=duration)  + timedelta(minutes=20)
            start_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
            duration_new = self.movie.duration
            new_time = timedelta(hours=self.time.hour, minutes=self.time.minute)
            new_time_end = timedelta(hours=self.time.hour, minutes=self.time.minute)+ timedelta(minutes=duration_new)  + timedelta(minutes=20)
           
            if Projection.time_in_range(start_time, end_time, new_time) or Projection.time_in_range(start_time, end_time, new_time_end):
                raise ValidationError("There is a projestion in this time")
    

class Ticket(models.Model):
    projection = models.ForeignKey(Projection, on_delete=models.SET_NULL, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=10, null=True)

    def qr_generator(self):

        data = {"id": self.id,
               "projection" : self.projection,
               "seat": self.seat,
               "user": self.user,
               "payment_method": self.payment_method
               } 
        
        img = qrcode.make(data)
        path = f"app/ticket_{self.id}.png"
        img.save(f"app/static/app/ticket_{self.id}.png")
        return path

    def __str__(self):
        return f"{self.projection} - {self.seat} {self.payment_method}"