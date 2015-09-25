import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from .models import Image
from .forms import ImageUploadForm


# Create your views here.
def MainPage(request):
	filteredimages = []
	sorttype = request.GET.get('sort',"")
	prevsort = request.GET.get('prevsort',"")
	datefilter = request.GET.get('datefilter', "")
	#response = HttpResponse();
	#response.write("Testing Again ")
	if(sorttype and datefilter):
	  pass
	else:
	  sorttype='ev_date'
	  datefilter='all'
	  prevsort='temp'
	if(sorttype=='name'):
	  if(prevsort=='name'):
	    images = sorted(Image.objects.all(), key=lambda image: image.name.lower(), reverse=True)
	    prevsort = "temp"
	  else:
	  	images = sorted(Image.objects.all(), key=lambda image: image.name.lower())
	  	prevsort = 'name'
	elif(sorttype=='pb_date'):
	  if(prevsort=='pb_date'):
	    images = sorted(Image.objects.all(), key=lambda image: image.date_published)
	    prevsort = "temp"
	  else:
	  	images = sorted(Image.objects.all(), key=lambda image: image.date_published, reverse=True)
	  	prevsort ='pb_date'
	elif(sorttype=='ev_date'):
	  if(prevsort=='ev_date'):
	    images = sorted(Image.objects.all(), key=lambda image: image.date_event)
	    prevsort = "temp"
	  else:
	  	images = sorted(Image.objects.all(), key=lambda image: image.date_event, reverse=True)
	  	prevsort = 'ev_date'
	else: images = Image.objects.all()
	datetoday = datetime.datetime.today().date()
	if(datefilter=='all'):
		filteredimages = images
	else:
		if(datefilter=="today"):
			for i in images:
				if(i.date_published.date()==datetoday):
					filteredimages+=[i]
		elif(datefilter=="thisweek" or datefilter=="thismonth"):
			if(datefilter=="thisweek"): timedelta = datetime.timedelta(days=7)
			else: timedelta = datetime.timedelta(days=30)
			for i in images:
				if(datetoday-i.date_published.date()<timedelta):
					filteredimages+=[i]
		else: filteredimages = images 
		#if(datefilter=='')

	context = {'images': filteredimages, 'sorttype':sorttype,'datefilter':datefilter, 'prevsort':prevsort}
	#return response
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
				




