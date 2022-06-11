from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hellodjango(request):

    return HttpResponse('Hello Django!')


def hellodjango_name(request, name):

    return HttpResponse(f'Hello {name}')


def django_date(request):

    return HttpResponse(f'{timezone.now().date()}')


def django_year(request):

    return HttpResponse(f'{timezone.now().year}')


def django_day(request):

    return HttpResponse(f'{timezone.now().day}')


def django_month(request):

    return HttpResponse(f'{timezone.now().month}')
