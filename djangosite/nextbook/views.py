from django.shortcuts import render
from django.http import HttpResponse

def suggestion(request):
    return HttpResponse("Get a reading suggestion: ")
