import requests
import random

from django.conf import settings
from django.utils import timezone

from playground import constants
from playground import models

"""
This is data access layer all the data extraction from db done here
"""


def fetch_results_from_youtube():
    query_parameter = random.choice(constants.QUERY_KEYWORD_LIST)
    search_params = {
        'part': 'snippet',
        'q': query_parameter,
        'maxResults': 40,
        'order': 'date',
        'publishedAfter': (timezone.now()-timezone.timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'key': settings.YOUTUBE_API_KEY
    }
    videos_data = requests.get(constants.YOUTUBE_SEARCH_URL, params=search_params)
    return videos_data.json()


def fetch_data_and_save_data_in_db():
    videos_data = fetch_results_from_youtube()
    for video in videos_data.get('items'):
        try:
            models.YouTubeVideo.objects.create(
                title = video.get('snippet').get('title'),
                description = video.get('snippet').get('description'),
                publishing_datetime = video.get('snippet').get('publishedAt'),
                thumbnail_urls = video.get('snippet').get('thumbnails'),
                youtube_id = video.get('id')         
            )
        except Exception as e:
            raise e


def get_data_for_videos():
    return list(models.YouTubeVideo.objects.all().order_by('publishing_datetime').values_list('title', 'description', 'thumbnail_urls'))


def get_data_for_video_search(search_term):
    return list(models.YouTubeVideo.objects.filter(title__icontains=search_term).values_list('title', 'description', 'thumbnail_urls'))