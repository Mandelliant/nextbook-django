from django.db import models
from django.forms import ModelForm
from nextbook.models import Book

class AddBook(ModelForm):
    class Meta:
        model = Book
        fields = ['book_number', 'title', 'author']






'''
Create the form class.
>>> class ArticleForm(ModelForm):
...     class Meta:
...         model = Article
...         fields = ['pub_date', 'headline', 'content', 'reporter']


form = AddBook()
# Creating a form to add an article.
>>> form = ArticleForm()


new_book = Book.objects.get(pk=1)
form = AddBook(instance=new_book)
# Creating a form to change an existing article.
>>> article = Article.objects.get(pk=1)
>>> form = ArticleForm(instance=article)
'''
