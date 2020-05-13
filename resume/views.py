from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .utils import render_to_pdf

from .models import Experience, Education
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
def education(request):
	user = request.user
	educations = Education.objects.filter(user=request.user)
	if experience:
		context = {
			'educations': educations,
		}
		return render(request, 'resume/education.html', context)
	return render(request, 'resume/education.html')

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
def settings(request):
	user = request.user
	profile = get_object_or_404(UserProfile, user=user)
	context = {
		'username': user.username,
		'email': user.email,
	}
	return render(request, 'resume/settings.html', context)

@login_required
def test(request, *args, **kwargs):
	experiences = Experience.objects.filter(user=request.user)
	educations = Education.objects.filter(user=request.user)
	print(educations[0])
	context = {
		'user_name': request.user.first_name + ' '  + request.user.last_name,
		'title': '',
		'about_me': '',
		'experiences': experiences,
		'educations': educations,
	}
	pdf = render_to_pdf('pdf/test.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		download = request.GET.get("download")
		print(download)
		if download == 'True':
			response['Content-Disposition'] = 'attachment; filename=test.pdf'
		return response
	return HttpResponse('PDF not found')
