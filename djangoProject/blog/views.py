from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def f_view(request):
    return HttpResponse('hello world')


def t_view(request, param, year=None):
    return HttpResponse(f'this parameter {param} and year is {year}')


