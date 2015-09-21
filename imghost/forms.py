from django import forms


class ImageUploadForm(forms.Form):
    imgfile = forms.ImageField(label='Select an Image')
    date_event = forms.DateTimeField(label = 'Event Date')