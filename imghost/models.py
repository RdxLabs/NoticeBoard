from django.db import models
# Create your models here.
class Image(models.Model):
	# image_thumb = ImageWithThumbsField(upload_to='images',sizes = ((200,150)))
	name = models.CharField(max_length=60, blank=True, null=True);
	image = models.FileField(upload_to='images/%Y/%m/%d')
	description = models.TextField(null=True)
	date_published = models.DateTimeField(auto_now_add = True)
##	date_edited = models.DateTimeField(auto_now = True)
	date_event = models.DateTimeField(null = True)

