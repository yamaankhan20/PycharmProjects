from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')


def about(request):
    return HttpResponse('this is about page')


def name_response(request, name):
    return HttpResponse(f'hi, {name.capitalize()}')