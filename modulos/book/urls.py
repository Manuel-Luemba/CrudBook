from django.shortcuts import path
from .  import views
app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
]