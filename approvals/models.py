from django.db import models
from .signals import tribute_approved, memory_approved, photo_approved


import logging
logr = logging.getLogger(__name__)

# Create your models here.


class TributeApproval(models.Model):
    approved = models.BooleanField(default=False)
    tribute_id = models.IntegerField()

    def save(self, **kwargs):
        if self.pk is not None and self.approved == True:
            rec = tribute_approved.send(self, tribute_id=self.tribute_id)
            logr.debug("Approval confirmed for tribute_id = %s" % self.tribute_id)

        super(TributeApproval, self).save(kwargs)







class MemoryApproval(models.Model):
    approved = models.BooleanField(default=False)
    memory_id = models.IntegerField()

    def save(self, **kwargs):
        if self.pk is not None and self.approved == True:
            rec = memory_approved.send(self,memory_id=self.memory_id)
            logr.debug("Approval confirmed for memory_id = %s" % self.memory_id)

        super(MemoryApproval, self).save(kwargs)








class PhotoApproval(models.Model):
    approved = models.BooleanField(default=False)
    photo_id = models.IntegerField()

    def save(self, **kwargs):
        if self.pk is not None and self.approved == True:
            rec = photo_approved.send(self,memory_id=self.photo_id)
            logr.debug("Approval confirmed for photo_id = %s" % self.photo_id)

        super(PhotoApproval, self).save(kwargs)        









