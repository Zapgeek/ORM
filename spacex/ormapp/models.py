
from django.db import models
from django.contrib import admin
class Movie(models.Model):
    Mid=models.CharField(max_length=20,help_text="Movie ID")
    Name=models.CharField(max_length=10)
    Genre=models.CharField(max_length=20)
    Rating=models.IntegerField()
    Collection=models.IntegerField()
    Year=models.IntegerField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('Mid','Name','Genre','Rating','Collection','Year')
    