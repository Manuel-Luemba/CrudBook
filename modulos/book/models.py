from django.db import models

class Book(models.Model):
    title = models.Charfield(max_lenght=50)
