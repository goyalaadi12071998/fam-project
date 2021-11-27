import requests

from django.conf import settings

from playground import constants
from playground import dal

def get_data_of_videos(search_term):
    if search_term == '':
        return dal.get_data_for_videos()
    return dal.get_data_for_video_search(search_term)