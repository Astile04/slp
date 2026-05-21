
from .serializers import LessonSerializer,CourseSerializer
from .models import Course
from rest_framework.viewsets import ModelViewSet

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filterset_fields = ['level','status']
    search_fields = ['title','description']
    ordering_fields = ['created_at']