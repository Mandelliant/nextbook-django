from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Book
from .forms import AddBook

def library(request):
    #return HttpResponse("Add a book to your library: ")

    #books = Book.objects.order_by('?').first()

    #Book.objects.random
    #books is the QuerySet variable, basically sets the variable books to be a random Book object from the model

    #form = AddBook()

    #return render(request, 'newbook/index.html', {'books': books})

    #return render(request, 'newbook/index.html')


    form = AddBook()

    if request.method == "POST":

        form = PostForm(request.POST)


    else:
        form = AddBook()

    return render(request, 'newbook/index.html', {'form': form})



def library(request):

    if request.method == "POST":

        form = AddBook(request.POST)

        if form.is_valid():
            addedbook = form.save(commit=False)
            addedbook.save()
    else:
        form = AddBook()
    return render(request, 'newbook/index.html', {'form': form})
