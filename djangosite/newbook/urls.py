from django.urls import path
from . import views

urlpatterns = [
    path('','newbook', views.index, name='index'),
]
