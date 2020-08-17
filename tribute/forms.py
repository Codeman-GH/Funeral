from django import forms
from . models import Tribute, Memory, Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit





class TributeForm(forms.ModelForm):

	class Meta:
		model = Tribute
		fields = ('name','message', 'image', 
            )





class MemoryForm(forms.ModelForm):

	class Meta:
		model = Memory
		fields = ('name','memories', 'message')


class PhotoForm(forms.ModelForm):

	class Meta: 
		model = Photo
		fields = ('name','image')
