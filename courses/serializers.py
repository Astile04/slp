from rest_framework import serializers
from .models import Lesson,Course

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id','title','order','is_free']




class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id','title','slug','description','level','status','instructor','lessons']
