from django.db import models
from django.utils import timezone
# Create your models here.


# creation of the required models for grade assingments

class Book(models.Model):
    name = models.CharField(max_length=200)
    page_number = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    published_date = models.DateField(timezone.now)


class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=1000)
    year = models.IntegerField(default=0)


def __str__(self):
    return self.name