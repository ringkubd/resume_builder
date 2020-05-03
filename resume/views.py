from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf


def home(request):
	return render(request, 'resume/homepage.html')


def test(request, *args, **kwargs):
	context = {
		'user_name': 'John Doe',
		'title': 'web developer',
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
