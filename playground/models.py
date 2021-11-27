from django.db import models
from jsonfield import JSONField

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    youtube_id = JSONField()
    publishing_datetime = models.DateTimeField()
    thumbnail_urls = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title