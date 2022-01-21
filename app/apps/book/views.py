from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from apps.book.models import Book



class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'

