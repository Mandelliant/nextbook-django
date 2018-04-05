from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Nextbook version 0.1.0")










'''
    return HttpResponse("What would you like to do? \n1. Add a new book \n2. Get a reading suggestion")

    menu_choice = input('Choose 1 or 2: ')
    selection = int(menu_choice)
'''
