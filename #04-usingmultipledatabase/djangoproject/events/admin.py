from django.contrib import admin
from .models import Event, MyClubUser, Venue
# Register your models here.

admin.site.register(Event)
admin.site.register(MyClubUser)
admin.site.register(Venue)
