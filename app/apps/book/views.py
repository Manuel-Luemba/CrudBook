from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(self):
    return HttpResponse("HOLA MUNDO DJANGO")