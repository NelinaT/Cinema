from django.db import models
capacity_for_hall_types = {
    "vip": {
        "rows": 5,
        "cols": 6
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
    duration = models.DurationField()
    genre = models.CharField(max_length=50)
    img_url = models.CharField(max_length = 100, default='')
    price = models.IntegerField(default = 10)
    def __str__(self):
        return self.name
    def toStr(self):
        return "{\n\tid: " + str(self.pk) + "\n\tname: "+ self.name +  "\n\tduration: "+ self.duration.__str__() + "\n\tgenre: "+ self.genre +"\n\timg_url: "+ self.img_url +"\n}"

class Projection(models.Model):
    start_date = models.DateTimeField()
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True)
    Hall = models.ForeignKey(Hall,on_delete=models.SET_NULL,null=True)

    @property
    def price(self):
        print(self.Hall.type)
        if self.Hall and self.movie:
            if self.Hall.type == "vip":
                return self.movie.price + 5
            if self.Hall.type == "std":
                return self.movie.price + 2
            if self.Hall.type == "big":
                return self.movie.price
        return 0        

    def __str__(self):
        return self.movie.name

class Seats_for_projection(models.Model):
    is_empty = models.BooleanField(default = True)
    projection = models.ForeignKey(Projection,on_delete=models.SET_NULL,null=True)
    seat = models.ForeignKey(Seat,on_delete=models.SET_NULL,null=True)
