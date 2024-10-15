# urls.py
from django.urls import path
from .views import create_checkout_session, PaymentListCreateView, SubscriptionListCreateView

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('payments/', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription_list_create'),
]