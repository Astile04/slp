from django.contrib import admin
from . models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display=['file_name','uploaded_by','file_type','file_size','uploaded_at']
    list_filter = ['file_type']