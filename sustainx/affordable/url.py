from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('bio-packaging', views.bio_packaging, name='about'),
    # path('investores-and-partners', views.investores_and_partners, name="greet"),
    # path('<str:name>', views.investores_and_partners, name="greet")
]