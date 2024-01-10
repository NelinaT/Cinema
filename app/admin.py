from django.contrib import admin
from .models import Hall,Seat,Movie,Projection,Seats_for_projection

admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Seats_for_projection)


# Register your models here.
