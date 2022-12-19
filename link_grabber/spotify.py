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

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    return access_token


BASE_URL = 'https://api.spotify.com/v1/'


def get_album(album_id):
    # Get an authentication token
    token = authenticate()

    # Add authentication token to the request headers
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token)
    }
    query_url = BASE_URL + f'albums/{album_id}'
    response = requests.get(query_url, headers=headers).json()
    return response


def get_track(track_id):
    # Get an authentication token
    token = authenticate()

    # Add authentication token to the request headers
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token)
    }
    query_url = BASE_URL + f'tracks/{track_id}'
    response = requests.get(query_url, headers=headers).json()
    return response


if __name__ == '__main__':
    pass
    # print(authenticate())
    # print(get_album('5BWl0bB1q0TqyFmkBEupZy'))
    # print(get_track('75FEaRjZTKLhTrFGsfMUXR'))
