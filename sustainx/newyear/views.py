from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, 'home-new/index.html', {
        'new': now.month == 8 and now.day == 18
    })