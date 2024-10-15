from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields chahiye User model me toh use this
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    verification_token = models.CharField(max_length=50, null=True, blank=True)
    # You can add more fields here like phone number, address, etc.
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username
