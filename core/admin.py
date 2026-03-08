from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import User, SiteSettings
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
    

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "content_type",)
    list_filter = ("content_type",)
    search_fields = ("name", "codename")

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "content", "updated_at")
    search_fields = ("title", "description")