from django.db import models
from django.conf import settings


class Course(models.Model):

    level_choices = [
        ('B', 'BEGINNER'),
        ('I', 'INTERMEDIATE'),
        ('A', 'ADVANCED'),
    ]

    status_choices = [
        ('D', 'DRAFT'),
        ('P', 'PUBLISHED'),
        ('A', 'ARCHIVED'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses_taught'
    )

    level = models.CharField(max_length=50, choices=level_choices)

    status = models.CharField(max_length=50, choices=status_choices)

    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'

    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Enrollment(models.Model):

    status_choices = [
        ('A', 'ACTIVE'),
        ('C', 'COMPLETED'),
        ('D', 'DROPPED'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='enrollments'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=50,
        choices=status_choices
    )

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"