# serializers.py
from rest_framework import serializers
from .models import Payment, Subscription

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'stripe_charge_id', 'amount', 'timestamp', 'success']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'stripe_subscription_id', 'active', 'start_date', 'end_date']