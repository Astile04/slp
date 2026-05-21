from django.db import models
from django.conf import settings

from courses.models import Course


class Task(models.Model):

    priority_choices = [
        ('L', 'LOW'),
        ('M', 'MEDIUM'),
        ('H', 'HIGH'),
        ('U', 'URGENT'),
    ]

    status_choices = [
        ('todo', 'TODO'),
        ('in_progress', 'IN PROGRESS'),
        ('done', 'DONE'),
        ('cancelled', 'CANCELLED'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    title = models.CharField(max_length=255)

    description = models.TextField(
        blank=True
    )

    priority = models.CharField(
        max_length=50,
        choices=priority_choices
    )
    status = models.CharField(
        max_length=50,
        choices=status_choices,
        default='todo'
    )

    due_date = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title