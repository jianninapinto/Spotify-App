import requests
from os import getenv


def authenticate():
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': getenv('CLIENT_ID'),
        'client_secret': getenv('CLIENT_SECRET')
    })
    print(auth_response)
    # convert the response to JSON
    auth_response_data = auth_response.json()
    print(auth_response_data)
    # save the access token
    access_token = auth_response_data['access_token']

    return access_token


print(authenticate())
