from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from menu.models import Book
from .forms import AddBook
from nextbook.models import Book
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

class BookAddConf(SuccessMessageMixin, CreateView):
    model = Book
    success_message = "%(new_title)s by %(new_author)s was added to your library"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            new_title=self.object.title,
            new_author=self.object.author
        )



def library(request):
    form = AddBook(request.POST or None)
    success = False
    if request.method == 'POST':
        if form.is_valid():
            addedbook = form.save(commit=False)
            addedbook.save()
            form = AddBook()
            success = True
            messages.success(request, "Added to your library")

            #new_title = get_success_message()


    return render(request, 'newbook/index.html', {'form': form})


'''
#all new below
class BookAddConf(SuccessMessageMixin, CreateView):
    model = Book
    success_message = "%(new_title)s by %(new_author)s was added to your library"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            new_title=self.object.title,
            new_author=self.object.author
        )





def get_success_message(self, cleaned_data):
    return "{} by {} has been added".format(cleaned_data['title', 'author'])
'''
