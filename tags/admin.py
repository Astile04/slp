from django.contrib import admin
from . models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['label','content_type','object_id']