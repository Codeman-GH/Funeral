from django.db import models
from django.utils import timezone
from funeral import settings
from django import forms
import datetime
from time import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from approvals.models import TributeApproval, MemoryApproval, PhotoApproval
from approvals.signals import tribute_approved, memory_approved, photo_approved



import logging

logr = logging.getLogger(__name__)


# Create models here.



def  get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()). replace('.', '_'), filename)





class Tribute(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.FileField(upload_to= get_upload_file_name)
    posted_on = models.DateTimeField('Date Posted')
    approved = models.BooleanField(default=False)


    def get_absolute_url(self):  
        from django.urls import reverse
        return reverse('tribute_details', args=[str(self.id)])
       


    def get_profile_picture(self):
        image = str(self.image)
        if not settings.DEBUG:
            image = image.replace('assets/','')

        return image
        



class Memory(models.Model):
    memories = 'memories'
    tributes = 'tributes'

    memories_choices = ((memories, 'Memories'),(tributes, 'Tributes'))
    


    name = models.CharField(max_length=100)
    memories = models.CharField(max_length=10, choices=memories_choices, default=memories)
    message = models.TextField()
    posted_on = models.DateTimeField('Date Posted')
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Memories"
        
    def get_absolute_url(self):  
        from django.urls import reverse
        return reverse('memory_details', args=[str(self.id)])
       






class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to = get_upload_file_name)
    posted_on = models.DateTimeField('Date Posted')
    appoved = models.BooleanField(default=False)



    def get_absolute_url(self):  
        from django.urls import reverse
        return reverse('photo_details', args=[str(self.id)])
       


    def get_profile_picture(self):
        image = str(self.image)
        if not setting.DEBUG:
            image = image.replace('assets/', '')


        return image







@receiver(post_save, sender=Tribute)
def create_approval_on_new_tribute(sender, **kwargs):
    if kwargs.get('created', False):
        tribute_approval = TributeApproval.objects.create(tribute_id=kwargs.get('instance').id)
        logr.debug("Tribute Approval created: %s" %tribute_approval)


@receiver(tribute_approved)
def approve_tribute(sender, **kwargs):
    at = Tribute.objects.get(id=kwargs.get('tribute_id'))
    at.approved = True
    at.save()
    logr.debug("Tribute Approved Accordingly")








@receiver(post_save, sender=Memory)
def create_approval_on_new_memory(sender, **kwargs):
    if kwargs.get('created', False):
       memory_approval = MemoryApproval.objects.create(memory_id=kwargs.get('instance').id)
       logr.debug("Memory Approval created: %s" %memory_approval)


@receiver(memory_approved)
def approve_memory(sender, **kwargs):
    am = Memory.objects.get(id=kwargs.get('memory_id'))
    am.approved = True
    am.save()
    logr.debug("Memory Approved Accordingly")








@receiver(post_save, sender=Photo)
def create_approval_on_new_photo(sender, **kwargs):
    if kwargs.get('created', False):
        photo_approval = PhotoApproval.objects.create(photo_id=kwargs.get('instance').id)
        logr.debug("Photo Approval created: %s" %photo_approval)


@receiver(photo_approved)
def approve_photo(sender, **kwargs):
    ap = Photo.objects.get(id=kwargs.get('photo_id'))
    ap.approved = True
    ap.save()
    logr.debug("Photo Approved Accordingly")












#OUR RECIEVER DECORATORS

    
    




    































    
        
    
