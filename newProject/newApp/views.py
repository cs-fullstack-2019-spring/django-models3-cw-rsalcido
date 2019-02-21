from django.shortcuts import render
# wrinting my first view
from django.http import HttpResponse
# Create your views here.

# this is the function I am calling above.

def index(request):
    return HttpResponse("Making shit happen at the house!"),
def Car(request):
    return HttpResponse("Making shit happen at the house!"),
def Book(request):
    return HttpResponse("Making shit happen at the house!"),
