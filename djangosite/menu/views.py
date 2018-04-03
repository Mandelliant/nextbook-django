from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Do you want a suggestion or to add a new book?")
