from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """
    Admin panel configuration for the User model.
    """
    list_display = ('email', 'name', 'role', 'is_active', 'is_staff', 'created_at', 'last_login')
    list_filter = ('role', 'is_active', 'is_staff', 'created_at')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Roles and Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
    readonly_fields = ('created_at', 'last_login')
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Activate selected users"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Deactivate selected users"


# Register the model
admin.site.register(User, UserAdmin)
