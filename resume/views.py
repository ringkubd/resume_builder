from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf

from .models import Experience, Education


def home(request):
	return render(request, 'resume/homepage.html')

@login_required
def profile(request):
	user = request.user
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
	}
	return render(request, 'resume/profile.html', context)


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
