from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role_choices = [
        ("ST","STUDENT"),
        ("IN","INSTRUCTOR"),
        ("AD","ADMIN"),
    ]

    role = models.CharField(max_length=20,choices=role_choices,default='ST')
    bio = models.TextField(max_length=100,blank=True,null=True)
    avatar = models.ImageField(null=True,upload_to='avatars/')
    date_of_birth = models.DateField(null=True)
    


    def __str__(self):
     return f"{self.username} - {self.role}"


    @property
    def is_instructor(self):
        return self.role == "IN"

