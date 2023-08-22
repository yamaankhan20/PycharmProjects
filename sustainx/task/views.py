from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

task=['foo','blaa','beat']
def index(request):
    return render(request, 'tasks-pages/index.html',{
        'tasks': task
    })


def add_tasks(request):
    return render(request, 'tasks-pages /add.html')