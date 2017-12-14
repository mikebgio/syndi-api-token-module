import requests
import json
import config #must create a config.py file in the same directory, See sample

def get_token(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, username=config.USERNAME, password=config.PASSWORD):
    get_token_files = {
        'grant_type': (None, 'password'),
        'client_id': (None, client_id),
        'client_secret': (None, client_secret),
        'scope': (None, 'read write'),
        'username': (None, username),
        'password': (None, password),
    }
    r = requests.post(
        'http://api.syndicaster.tv/oauth/access_token',
        files=get_token_files)
    pjson = json.loads(r.text)
    ACCESS_TOKEN = pjson['access_token']
    REFRESH_TOKEN = pjson['refresh_token']
    return(ACCESS_TOKEN, REFRESH_TOKEN)


def refresh(refresh_token, client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET):
    refresh_token_files = {
        'grant_type': (None, 'refresh_token'),
        'client_id': (None, client_id),
        'client_secret': (None, client_secret),
        'refresh_token': (None, refresh_token)
    }
    r = requests.post(
        'http://api.syndicaster.tv/oauth/access_token',
        files=refresh_token_files)
    pjson = json.loads(r.text)
    ACCESS_TOKEN = pjson['access_token']
    REFRESH_TOKEN = pjson['refresh_token']
    return(ACCESS_TOKEN, REFRESH_TOKEN)
