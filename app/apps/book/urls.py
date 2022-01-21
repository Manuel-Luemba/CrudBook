from django.urls import path
from apps.book.views import *

app_name = 'lib'
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
]
