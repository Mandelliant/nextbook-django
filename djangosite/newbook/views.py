from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from menu.models import Book
from .forms import AddBook
from nextbook.models import Book
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView



def library(request):
    form = AddBook(request.POST or None)
    success = False
    if request.method == 'POST':
        if form.is_valid():
            addedbook = form.save(commit=False)
            addedbook.save()
            #form = AddBook()
            success = True
            nbt = form.cleaned_data['title']
            nba = form.cleaned_data['author']
            messages.success(request, "{} by {} added to your library".format(nbt, nba))

            #new_title = get_success_message()


    return render(request, 'newbook/index.html', {'form': form})
