
from django.contrib import admin
from django.urls import path, include

from resume import views

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('test', views.test, name='test'),
]
