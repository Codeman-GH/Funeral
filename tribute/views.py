from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Tribute, Memory, Photo
from .forms import TributeForm,MemoryForm, PhotoForm
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
    if request.method == 'POST':
        form_tribute = TributeForm(request.POST, request.FILES)  
        if form_tribute.is_valid():
            
            p = form_tribute.save(commit = False)
            p.posted_on = timezone.now()
            p.save()
                        
            return HttpResponseRedirect('/tribute_list')

    else:
        form_tribute = TributeForm()
        args = {}


        args['form_tribute'] = form_tribute,


    if request.method == 'POST':
        form_memory = MemoryForm(request.POST)
        if form_memory.is_valid():
            p = form_memory.save(commit = False)
            p.posted_on = timezone.now()
            p.save()
                        
            return HttpResponseRedirect('/memory_list')

    else:
        form_memory = MemoryForm()


    args = {}


    args['form_memory'] = form_memory,






    if request.method == 'POST':
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

    return render(request, 'tribute/homepage.html', {
                'form_tribute': form_tribute,
                'form_memory': form_memory,
                'form_photo': form_photo,
                


 })







def biography(request):
    return render(request, 'tribute/biography.html', {

})



def tribute_list(request, id=1):
    tributes = Tribute.objects.all()
    return render(request, 'tribute/tribute_list.html', {

    'tributes': tributes,
})
    

def memory_list(request, id=1):
    memories = Memory.objects.all()
    return render(request, 'tribute/memory_list.html', {

    'memories': memories,
})


def photo_list(request, id=1):
    photos = Photo.objects.all()
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





