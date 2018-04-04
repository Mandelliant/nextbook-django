from django.shortcuts import render
from django.http import HttpResponse

def lib(request):
    return HttpResponse("Add a book to your library: ")
