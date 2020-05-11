
from django.contrib import admin
from django.urls import path, include

from resume import views

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('profile/update_user', views.update_user, name='update_user'),
    path('experience', views.experience, name='experience'),
    path('experience/update_experience', views.update_experience, name='update_experience'),
    path('experience/create_experience', views.create_experience, name='create_experience'),
    path('education', views.education, name='education'),
    path('education/update_education', views.update_education, name='update_education'),
    path('education/create_education', views.create_education, name='create_education'),
    path('settings', views.settings, name='settings'),
    path('test', views.test, name='test'),
]
