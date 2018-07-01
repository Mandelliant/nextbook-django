from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Book

def library(request):
    #return HttpResponse("Add a book to your library: ")

    #books = Book.objects.random
    #books is the QuerySet variable, basically sets the variable books to be a random Book object from the model

    #return render(request, 'newbook/index.html', {'books': books})

    return render(request, 'newbook/index.html')
