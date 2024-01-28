from django.urls import path
from . import views

urlpatterns=[
    path('/',views.home, name='home'),
    path('chat/',views.gchat, name='chat'),
    path('gemplans/',views.gemplans, name='gemplans')
]