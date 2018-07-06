from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from menu.models import Book
from .forms import AddBook


def library(request):

    if request.method == 'POST':

        form = AddBook(request.POST)

        if form.is_valid():
            addedbook = form.save(commit=False)
            addedbook.save()
            return HttpResponseRedirect('/newbook/')

    else:
        form = AddBook()

    return render(request, 'newbook/index.html', {'form': form})
