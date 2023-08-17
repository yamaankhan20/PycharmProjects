from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'sustain-home/index.html')


def bio_packaging(request):
    return render(request, 'sustain-home/bio-packaging.html')


def investores_and_partners(request, name):
    return render(request, 'sustain-home/investores-and-partners.html', {
        'name': name.capitalize()
    })