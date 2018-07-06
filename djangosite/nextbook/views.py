from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

def suggestion(request):
    #Book.objects.random
    #books is the QuerySet variable, basically sets the variable books to be a random Book object from the model

    books = Book.get_random()

    return render(request, 'nextbook/index.html', {'books': books})
