from django.urls import path
from . import views

urlpatterns = [
    path('','nextbook', views.index, name='index'),
]
