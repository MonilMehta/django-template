# signals.py
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from django.utils.crypto import get_random_string

@receiver(post_save, sender=CustomUser)
def send_verification_otp(sender, instance, created, **kwargs):
    if created and not instance.is_active:  # Only send OTP if user is inactive
        otp = get_random_string(length=6, allowed_chars='0123456789')
        instance.verification_token = otp
        instance.save()

        subject = "Verify your email with OTP"
        message = f"Your OTP for verification is: {otp}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
