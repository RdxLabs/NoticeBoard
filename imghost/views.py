from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Image
from .forms import ImageUploadForm


# Create your views here.
def MainPage(request):
	images = Image.objects.all()
	context = {'images': images}
	return render_to_response('mainpage.html',context,context_instance = RequestContext(request))

def UploadPage(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		date_event = request.GET.get('date_event')
		new_image = Image(image = request.FILES['imgfile'],date_event = date_event )
		new_image.save()
		return HttpResponseRedirect('http://127.0.0.1:8000')	#use HttpResponserRedirect('/')
	else:
		form = ImageUploadForm()
		context = {'form' : form }
		return render_to_response('uploadpage.html',context,context_instance = RequestContext(request))
				




