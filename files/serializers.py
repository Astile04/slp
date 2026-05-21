from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = File
        fields = ['id','file','file_name','file_type','file_size','uploaded_at','uploaded_by']

