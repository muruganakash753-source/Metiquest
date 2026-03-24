from django.contrib import admin
from .models import Coordinator, Event, Gallery, SiteSetting

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'contact_number')
    list_filter = ('role',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'start_time', 'end_time', 'max_members')
    list_filter = ('category',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'uploaded_at')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('registration_link', 'is_active')