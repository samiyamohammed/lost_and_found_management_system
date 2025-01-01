from django.contrib import admin
from .models import LostItem, FoundItem

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date_lost', 'user_id', 'created_at')
    search_fields = ('name', 'location')

@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date_found', 'user_id', 'created_at')
    search_fields = ('name', 'location')
