from django.contrib import admin

from playground import models

@admin.register(models.YouTubeVideo)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'publishing_datetime')
    search_fields = ('title',)
    list_filter = ('publishing_datetime',)
    ordering = ('publishing_datetime',)
    readonly_fields = ('created_at', 'updated_at', 'publishing_datetime', 'youtube_id')