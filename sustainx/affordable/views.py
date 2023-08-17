from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'sustain-home/index.html')


def bio_packaging(request):
    return render(request, 'sustain-inner/bio-packaging.html')


def investores_and_partners(request):
    return render(request, 'sustain-inner/investores-and-partners.html')
