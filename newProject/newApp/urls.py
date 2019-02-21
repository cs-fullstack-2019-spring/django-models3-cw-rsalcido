from django.urls import path
# creating links for import
from .import views

urlpatterns=[
    path("", views.index, name="index"),
    path("Car", views.Car, name="index"),
    path("Book", views.Book, name="index"),

]