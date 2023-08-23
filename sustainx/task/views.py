from asyncio import tasks
import asyncio
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.


class NewTaskForms(forms.Form):
    task = forms.CharField(label='new task')

def index(request):
    if 'all_tasks' not in request.session:
        request.session['all_tasks']=[]
    return render(request, 'tasks-pages/index.html',{
        'tasks_list': request.session['all_tasks']
    })


def add_tasks(request):
    if request.method == 'POST':
        form_detials = NewTaskForms(request.POST)
        if form_detials.is_valid():
            task_data = form_detials.cleaned_data['task']
            request.session['all_tasks'] += [task_data]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return (request,'tasks-pages/add.html',{
                'form': form_detials
            })
    return render(request, 'tasks-pages/add.html',{
        'form': NewTaskForms()
    })