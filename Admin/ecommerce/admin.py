from django.contrib import admin
from .models import Movie

# Register your models here.
class Movieadmin(admin.ModelAdmin):
    list_display = ('name','duration','grade','type','price') # list
    search_fields = ('name',)
    list_filter = ('type',)
    list_per_page = 15

admin.site.register(Movie,Movieadmin)
