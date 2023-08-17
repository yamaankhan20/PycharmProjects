from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    dates_now = datetime.datetime.now()
    return render(request, 'newyea/index.html', {
        'newyear': dates_now.month == 1 and dates_now.day == 1
    })