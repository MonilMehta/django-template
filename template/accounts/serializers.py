from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'date_of_birth', 'profile_image', 'phone_number', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class VerifyOTPSerializer(serializers.Serializer):
    username = serializers.CharField()
    otp = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        otp = data.get('otp')
        
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('User does not exist')
        
        # Assuming you have a field `verification_token` to store the OTP
        if user.verification_token != otp:
            raise serializers.ValidationError('Invalid OTP')
        
        return data

    def save(self, **kwargs):
        username = self.validated_data['username']
        user = CustomUser.objects.get(username=username)
        user.is_active = True  # Mark the user as active
        user.verification_token = ''  # Clear the OTP
        user.save()
        return user

    
class ResendVerificationSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('User does not exist')
        
        if user.is_active:
            raise serializers.ValidationError('User is already verified')
        
        return data