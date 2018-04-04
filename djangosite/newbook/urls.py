from django.urls import path
from . import views

urlpatterns = [
    path('','newbook/', views.lib, name='library'),
]
