from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('form', views.Myform, name='form'),
]
