from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf


def home(request):
	return render(request, 'resume/homepage.html')

def profile(request):
	return render(request, 'resume/profile.html')


def test(request, *args, **kwargs):
	print(request)
	context = {
		'user_name': request.POST["firstName"] + ' '  + request.POST["lastName"],
		'title': request.POST["title"],
		'about_me': '',
		'experience': '',
		'education': '',
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
