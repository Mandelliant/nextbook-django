from django.shortcuts import render
from django.http import HttpResponse

def library(request):
    return HttpResponse("Add a book to your library: ")
