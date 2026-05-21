from django.db import models
from django.conf import settings

def upload_path(instance,filename):
    return f"uploads/{instance.uploaded_by.username}/{filename}"

class File(models.Model):

    type_choices = [
        ('I','IMAGE'),
        ('D','DOCUMENT'),
        ('V','VIDEO'),
        ('O','OTHER'),
    ]


    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='files'
    )

    file = models.FileField(upload_to=upload_path)

    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=50,choices=type_choices)

    file_size = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name