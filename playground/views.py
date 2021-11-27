import requests
import json

from django.http import HttpResponse
from django.core.paginator import Paginator

from playground import private
from playground import public
from playground import constants

def get_data(request):
    
    if request.method == 'GET':
        page_number = request.GET.get('page_number')
        search_term = request.GET.get('search_term') or ''
        data_for_videos = private.get_data_of_videos(search_term)
        data_for_current_page = public.get_data_for_current_page(data_for_videos, page_number, constants.DATA_PER_PAGE)
        response = {
            'status': 200,
            'data': data_for_current_page,
        }
        return HttpResponse(data_for_current_page)
    
    else:
        status = 400
        message = 'Bad Request'
        response = {'status': status, 'message': message}
        return HttpResponse(response)