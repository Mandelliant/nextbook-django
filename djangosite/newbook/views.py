from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Book
from .forms import AddBook

def library(request):

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
