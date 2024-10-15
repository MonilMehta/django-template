from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Specify the fields to display in the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'bio', 'date_of_birth')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'date_of_birth', 'profile_image', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
