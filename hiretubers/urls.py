from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('hiretuber',views.hiretuber,name="hiretuber")

 
]