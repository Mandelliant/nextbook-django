from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Add a book to your library: ")
