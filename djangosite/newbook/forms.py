from django import forms
from django.db import models
from django.forms import ModelForm
from nextbook.models import Book
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView



#use messages framework to create success message class
#figure out how to get success message in the view/template

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_number', 'title', 'author']


class ComplicatedCreate(SuccessMessageMixin, CreateView):
    model = Book
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )
