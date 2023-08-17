from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('<str:name>', views.name_response, name="greet")
]