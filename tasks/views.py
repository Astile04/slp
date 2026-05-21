from .serializers import TaskSerializer
from .models import Task
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = ['status','priority']
    search_fields = ['title']
    ordering_fields = ['due_date','priority']


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        