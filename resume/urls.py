
from django.contrib import admin
from django.urls import path, include

from resume import views

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('profile/update_user', views.update_user, name='update_user'),
    
    path('experience', views.experience, name='experience'),
    path('experience/create_experience', views.create_experience, name='create_experience'),
    path('experience/update_experience', views.update_experience, name='update_experience'),
    path('experience/delete_experience/<int:id>', views.delete_experience, name='delete_experience'),

    path('education', views.education, name='education'),
    path('education/create_education', views.create_education, name='create_education'),
    path('education/update_education', views.update_education, name='update_education'),
    path('education/delete_education/<int:id>', views.delete_education, name='delete_education'),

    path('skills', views.skills, name='skills'),
    path('skills/create_skill', views.create_skill, name='create_skill'),
    path('skills/delete_skill/<int:id>', views.delete_skill, name='delete_skill'),

    path('settings', views.settings, name='settings'),
    path('generate_resume', views.generate_resume, name='generate_resume'),
]
