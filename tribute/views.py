from django.shortcuts import render, render, get_object_or_404
from django.utils import timezone
from .models import Tribute, Memory, Photo
from .forms import TributeForm, MemoryForm, PhotoForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.backends import *
#from haystack.query import SearchQuerySet
from django.template import RequestContext
from django.contrib import messages 
from django.conf import settings
#from django.contrib import auth
#from django.contrib.auth.models import User
from django.core.paginator import Paginator 


#Create views here.
def homepage(request):





        



######################################


    if request.method == 'POST' and 'btnTribute' in request.POST:
        
        tribute_form = TributeForm(request.POST, request.FILES)
        
        if tribute_form.is_valid():
            p = tribute_form.save(commit =False)
            p.posted_on = timezone.now()
            p.save()
           

            return HttpResponseRedirect('/tribute_list')
    else:
        tribute_form = TributeForm()


        args ={}

        args['tribute_form'] = tribute_form





    

###########################################


##############################


    if request.method == 'POST' and 'btnPhoto' in request.POST:
        form_photo = PhotoForm(request.POST, request.FILES)
        if form_photo.is_valid():
            p = form_photo.save(commit = False)
            p.posted_on = timezone.now()
            p.save()
            
                        
            return HttpResponseRedirect('/photo_list')

    else:
        form_photo = PhotoForm()


    args = {}


    args['form_photo'] = form_photo,


 




    if request.method == 'POST' and 'btnMemory' in request.POST:
        memory_form = MemoryForm(request.POST)  
        if memory_form.is_valid():
            
            
            
            mf =memory_form.save(commit = False)
            mf.posted_on = timezone.now()
            mf.save()

            
                        
            return HttpResponseRedirect('/memory_list')

    else:
        memory_form = MemoryForm()
        args = {}


        args['memory_form'] = memory_form,





    

    return render(request, 'tribute/homepage.html', {
                'tribute_form': tribute_form,
                'form_photo': form_photo,
                 'memory_form': memory_form,

 }






 )











def biography(request):
    return render(request, 'tribute/biography.html', {

})



def tribute_list(request, id=1):
    tributes = Tribute.objects.all().order_by('-id')
    return render(request, 'tribute/tribute_list.html', {

    'tributes': tributes,
})
    

def memory_list(request, id=1):
    memories = Memory.objects.all().order_by('-id')
    return render(request, 'tribute/memory_list.html', {

    'memories': memories,
})


def photo_list(request, id=1):
    photos = Photo.objects.all().order_by('-id')
    return render(request, 'tribute/photo_list.html', {

    
    'photos': photos,
})

##########################################




def tribute_details(request, id):
    tribute = get_object_or_404(Tribute, id=id)
    return render(request, 'tribute/tribute_details.html', {

    'tribute': tribute,

})


def memory_details(request, id):
    memory = get_object_or_404(Memory, id=id)
    return render(request, 'tribute/memory_details.html', {

    'memory': memory,

})




def photo_details(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'tribute/photo_details.html', {

    'photo': photo,

})


#######################################################


 

##
##def tribute_add(request):
##    if request.method == 'POST':
##
##        form_tribute = TributeForm(request.POST, request.FILES)
##        if form_tribute.is_valid():
##            p = form_tribute.save(commit = False)
##            p.posted_on = timezone.now()
##            p.save()
##                        
##            return HttpResponseRedirect('/tribute_list')
##
##    else:
##        form_tribute = TributeForm()
##
##
##    args = {}
##
##
##    args['form'] = form,
##
##    return render(request, 'tribute/tribute_add.html', {
##        'form': form,
##
##
##})




##def memory_add(request):
##    if request.method == 'POST':
##
##        form = MemoryForm(request.POST)
##        if form.is_valid():
##            p = form.save(commit = False)
##            p.posted_on = timezone.now()
##            p.save()
##                        
##            return HttpResponseRedirect('/memory_list')
##
##    else:
##        form = MemoryForm()
##
##
##    args = {}
##
##
##    args['form'] = form,
##
##    return render(request, 'tribute/memory_add.html', {
##        'form': form,
##
##
##})




##
##def photo_add(request):
##    if request.method == 'POST':
##
##        form = PhotoForm(request.POST, request.FILES)
##        if form.is_valid():
##            p = form.save(commit = False)
##            p.posted_on = timezone.now()
##            p.save()
##                        
##            return HttpResponseRedirect('/photo_list')
##
##    else:
##        form = PhotoForm()
##
##
##    args = {}
##
##
##    args['form'] = form,
##
##    return render(request, 'tribute/photo_add.html', {
##        'form': form,
##
##
##})
##





