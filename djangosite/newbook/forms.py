from django import forms
from django.db import models
from django.forms import ModelForm
from nextbook.models import Book



#use messages framework to create success message class
#figure out how to get success message in the view/template

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_number', 'title', 'author']
