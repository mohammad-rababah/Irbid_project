from django.db import models

# Create your models here.
# table ---> student
from django.db.models import Model


class Student(Model):
    first_name = models.CharField(max_length=100)  # str
    last_name = models.CharField(max_length=100)  # str
    avg = models.FloatField()
    age = models.IntegerField()