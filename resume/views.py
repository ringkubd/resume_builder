from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .utils import render_to_pdf

from .models import Experience, Education, Skill
from user_profile.models import UserProfile


def home(request):
	return render(request, 'resume/homepage.html')

@login_required
def profile(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	context = {
		'username': user.username,
		'email': user.email,
		'phone': profile.phone,
		'profession': profile.profession,
		'bio': profile.bio
	}
	return render(request, 'resume/profile.html', context)

@login_required
def update_user(request):
	user = request.user
	user.username = request.POST['username']
	user.email = request.POST['email']
	user.save()
	profile = get_object_or_404(UserProfile, user=user)
	profile.phone = request.POST['phone']
	profile.profession = request.POST['profession']
	profile.bio = request.POST['bio']
	profile.save()
	return HttpResponseRedirect(reverse('resume:profile'))

################################# CRUD EXPERIENCE

@login_required
def experience(request):
	user = request.user
	experiences = Experience.objects.filter(user=request.user)
	if experience:
		context = {
			'experiences': experiences,
		}
		return render(request, 'resume/experience.html', context)
	return render(request, 'resume/experience.html')

@login_required
def create_experience(request):
	experience = Experience()
	experience.user = request.user
	experience.company = request.POST['company']
	experience.role = request.POST['role']
	experience.startDate = request.POST['start']
	experience.endDate = request.POST['end']
	experience.description = request.POST['description']
	experience.save()
	return HttpResponseRedirect(reverse('resume:experience'))

@login_required
def update_experience(request):
	id = request.POST['id']
	experience =get_object_or_404(Experience, id=id)
	experience.company = request.POST['company']
	experience.role = request.POST['role']
	# experience.startDate = request.POST['start']
	# experience.endDate = request.POST['end']
	experience.description = request.POST['description']
	experience.save()
	return HttpResponseRedirect(reverse('resume:experience'))

@login_required
def delete_experience(request, id):
	experience = get_object_or_404(Experience, id=id)
	experience.delete()
	return HttpResponseRedirect(reverse('resume:experience'))

################################# CRUD EDUCAION 

@login_required
def education(request):
	user = request.user
	educations = Education.objects.filter(user=request.user)
	if educations:
		context = {
			'educations': educations,
		}
		return render(request, 'resume/education.html', context)
	return render(request, 'resume/education.html')

@login_required
def create_education(request):
	education = Education()
	education.user = request.user
	education.school = request.POST['school']
	education.degree = request.POST['degree']
	education.startDate = request.POST['start']
	education.endDate = request.POST['end']
	education.description = request.POST['description']
	education.save()
	return HttpResponseRedirect(reverse('resume:education'))

@login_required
def update_education(request):
	id = request.POST['id']
	education =get_object_or_404(Education, id=id)
	education.school = request.POST['school']
	education.degree = request.POST['degree']
	# education.startDate = request.POST['start']
	# education.endDate = request.POST['end']
	education.description = request.POST['description']
	education.save()
	return HttpResponseRedirect(reverse('resume:education'))

@login_required
def delete_education(request, id):
	education = get_object_or_404(Education, id=id)
	education.delete()
	return HttpResponseRedirect(reverse('resume:education'))


################################# CRUD SKILL

@login_required
def skills(request):
	user = request.user
	skills = Skill.objects.filter(user=request.user)
	skills = skills[::-1] ##reversing the list
	context = {
		'skills': skills,
	}
	return render(request, 'resume/skills.html', context)

@login_required
def create_skill(request):
	skill = Skill()
	skill.user = request.user
	skill.name = request.POST['name']
	skill.save()
	return HttpResponseRedirect(reverse('resume:skills'))

@login_required
def delete_skill(request, id):
	skill = get_object_or_404(Skill, id=id)
	skill.delete()
	return HttpResponseRedirect(reverse('resume:skills'))


################################# SETTINGS

@login_required
def settings(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	context = {
		'username': user.username,
		'email': user.email,
	}
	return render(request, 'resume/settings.html', context)

################################# BUILD RESUME

@login_required
def generate_resume(request, *args, **kwargs):
	profile = get_object_or_404(UserProfile, user=request.user)
	experiences = Experience.objects.filter(user=request.user)
	educations = Education.objects.filter(user=request.user)
	skills = Skill.objects.filter(user=request.user)
	context = {
		'full_name': request.user.first_name + ' '  + request.user.last_name,
		'profession': profile.profession,
		'about_me': profile.bio,
		'experiences': experiences,
		'educations': educations,
		'skills': skills,
	}
	pdf = render_to_pdf('pdf/test.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		download = request.GET.get("download")
		if download == 'True':
			response['Content-Disposition'] = 'attachment; filename=test.pdf'
		return response
	return HttpResponse('PDF not found')

