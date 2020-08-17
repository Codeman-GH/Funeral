from django.contrib import admin

from .models import TributeApproval, MemoryApproval, PhotoApproval
# Register your models here.

##
##class TributeApprovalAdmin(admin.ModelAdmin):
##    list_display = ['approved', 'tribute_id' ]
##
##
##class MemoryApprovalAdmin(admin.ModelAdmin):
##    list_display = ['approved', 'memory_id' ]
##
##
##class PhotoApprovalAdmin(admin.ModelAdmin):
##    list_display = ['approved', 'photo_id' ]
##
##
##admin.site.register(TributeApproval, TributeApprovalAdmin)
##admin.site.register(MemoryApproval, MemoryApprovalAdmin)
##admin.site.register(PhotoApproval, PhotoApprovalAdmin)
