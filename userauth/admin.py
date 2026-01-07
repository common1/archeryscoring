from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm  # new
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = AdminUserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['display_name', 'email', 'first_name', 'last_name']
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     ("Custom", {'fields': ('display_name', 'date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'photo',)}),
    # )
    fieldsets = UserAdmin.fieldsets + (
        ("Custom", {'fields': ('display_name', 'date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'photo',)}),
    )

