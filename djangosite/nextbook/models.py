from django.db import models

# Create your models here.

class Book(models.Model):
    book_number = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
