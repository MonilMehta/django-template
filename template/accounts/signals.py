# signals.py
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from django.utils.crypto import get_random_string

@receiver(post_save, sender=CustomUser)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        verification_token = get_random_string(length=32)
        instance.verification_token = verification_token
        instance.save()

        verification_link = f"http://localhost:8000/verify-email/{verification_token}"
        subject = "Verify your email"
        message = f"Please click the following link to verify your email: {verification_link}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])

