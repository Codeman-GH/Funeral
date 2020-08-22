from django import forms

from . models import Tribute, Memory, Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit





class TributeForm(forms.ModelForm):
        
        
        
                
        class Meta:
                


                
                                
                model = Tribute
                fields = ('name','message', 'image', 
            )

                widgets = {
                        
                'name': forms.TextInput(attrs={'autofocus': 'on' ,'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Name...'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Your tribute goes here...', 'cols':5, 'rows': 10}),
               # 'image': forms.File(attrs={'class': 'form-control'}),


                }    







class MemoryForm(forms.ModelForm):

        class Meta:
                model = Memory
                fields = ('name', 'message')


                widgets = {
                        
                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Name...'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Memory goes here...'}),
 }    



class PhotoForm(forms.ModelForm):
        

        class Meta: 
                model = Photo
                fields = ('name','image')



                widgets = {

                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Name...'}),
           
 }    
