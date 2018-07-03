from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

def suggestion(request):
    #return HttpResponse("Get a reading suggestion: Yes or no?")
    #books = Book.objects.order_by('?').first()
    #Book.objects.random
    #books is the QuerySet variable, basically sets the variable books to be a random Book object from the model


    #random_index = randrange(0,len(randoms))


    books = Book.randoms.all()[0]

    #books = Book.random.choice(randoms)


    return render(request, 'nextbook/index.html', {'books': books})
