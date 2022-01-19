from django.shortcuts import render
from django.http import HttResponse

def index(self):
    return HttResponse("Hola mundo")
