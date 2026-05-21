from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import FileSerializer
from .models import File
class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(uploaded_by=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(uploaded_by=self.request.user)