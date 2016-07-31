from django.shortcuts import render
from django.http import HttpResponse

# api function imports
import requests
import sys
import traceback
import time
import json

# api variables
ANICLIENT = ''
ANISECRET = ''

access_token = ''

# Create your views here.

def index(request):
    response = "This is the series index"
    return HttpResponse(response)

def series_view(request, id):
    # TODO
        # Get series model by some id in url or 404
        # Get synopsis and other info about series
        # Get viewing information(if any)
        # Render all
    response = "This is the viewings page for the series %s" % id
    return HttpResponse(response)

def series_lib(request, id):
    # TODO
        # Get series model by some id in url or 404
        # Get synopsis and other info about series
        # Get item models for this series
        # Work out status of each item
        # Render all
    response = "This is the library page for the series %s" % id
    return HttpResponse(response)

def check_and_get_old_api_token():
    try:
        # open the file if it exists
        token_file = open('anilist.token', 'r+')
        token_json = json.load(token_file)
        time_now = time.time()

        if time_now < token_json['expires']:
            # old token invalid
            global access_token
            access_token = token_json['access_token']
            token_file.close()
            return True
        else:
            # token in file is invalid
            token_file.close()
            return False

    except Exception as e:
        # Token file doesnt exist or there was some other error
        # create a new empty token file
        open('anilist.token', 'w').close()
        return False

def get_new_api_token():
    try:
        request = requests.post('https://anilist.co/api/auth/access_token', params={'grant_type':'client_credentials', 'client_id':ANICLIENT, 'client_secret':ANISECRET})

        # write token to file
        request_json = request.json()
        f = open('anilist.token', 'w')
        json.dump(request_json, f)
        f.close()

        # set global variable
        global access_token
        access_token = request_json['access_token']
    except Exception as e:
        # oh noes!

def api_setup():
    if check_and_get_old_api_token():
        return
    else:
        get_new_api_token()

def api_get_info(media_id, media_type):
    url = 'https://anilist.co/api/'
    if media_type == 'anime':
        url += 'anime/'
    elif media_type == 'manga':
        url += 'manga/'
    else:
        # function wasnt called with the media_type variable
        return None

    try:
        request = requests.get(url+ str(media_id), params={'access_token':access_token})

        if request.status_code == 401:
            api_setup()
            request = requests.get(url + str(media_id), params={'access_token':access_token})
        
        if request.status_code == 200:
            return request.json()
        else:
            return None
    except Exception as e:
        # function wasnt called with the media_id variable
        return None