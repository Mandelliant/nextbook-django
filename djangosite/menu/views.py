from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Nextbook version 0.1.0")

    return render(request, 'menu/index.html', {})
