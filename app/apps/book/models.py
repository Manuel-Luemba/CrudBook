from django.db import models
from apps.book.choices import BOOK_TYPES

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank = True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
  

