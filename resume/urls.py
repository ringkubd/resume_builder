
from django.contrib import admin
from django.urls import path, include

from resume import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
]
