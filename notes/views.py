from .serializers import NoteSerializer
from .models import Note

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title','body']
    ordering_fields = ['created_at','is_pinned']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)