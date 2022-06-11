from django.contrib import admin
from django.urls import path

from .views import hellodjango, hellodjango_name, django_date, django_day, django_year, django_month

urlpatterns = [
   path('/', hellodjango, name='hello'),
   path('date/', django_date, name='django_date'),
   path('year/', django_year, name='django_year'),
   path('month/', django_month, name='django_month'),
   path('day/', django_day, name='django_day'),
   path('<str:name>/', hellodjango_name, name='hello_name'),
]