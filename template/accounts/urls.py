# urls.py
from django.urls import path
from .views import RegisterView, LoginView, RefreshView, VerifyOTPView, ResendVerificationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshView.as_view(), name='token_refresh'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('resend-verification/', ResendVerificationView.as_view(), name='resend-verification'),

]