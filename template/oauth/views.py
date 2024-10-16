from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'oauth/login.html')

@login_required
def profile(request):
    return render(request, 'oauth/profile.html')