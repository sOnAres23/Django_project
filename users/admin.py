from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'phone_number', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'first_name', 'last_name', 'phone_number', 'avatar')}),

        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'phone_number', 'avatar', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'username',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
