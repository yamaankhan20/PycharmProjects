from asyncio import tasks
import asyncio
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django import forms
# Create your views here.

all_task=['foo','blaa','beat']

class NewTaskForms(forms.Form):
    task = forms.CharField(label='new task')

def index(request):
    return render(request, 'tasks-pages/index.html',{
        'tasks_list': all_task
    })


def add_tasks(request):
    if request.method == 'POST':
        form_detials = NewTaskForms(request.POST)
        if form_detials.is_valid():
            task_data = form_detials.cleaned_data['task']
            all_task.append(task_data)
        else:
            return (request,'tasks-pages/add.html',{
                'form': form_detials
            })
    return render(request, 'tasks-pages/add.html',{
        'form': NewTaskForms()
    })