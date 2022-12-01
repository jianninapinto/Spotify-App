import requests
from spotify import authenticate


# Spotify global top 50 playlist: https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF

def get_top_50_links():

    # Get an authentication token
    token = authenticate()

    # Add authentication token to the request headers
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    query_url = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF'

    # Query the Spotify API for the playlist
    response = requests.get(query_url, headers=headers)
    # Parse the response into a dictionary (JSON)
    response = response.json()

    # Exploring the response object's structure

    # print(response)
    # print(len(response))
    # print(response.keys())
    # print(response['tracks'])
    # print(len(response['tracks']))
    # print(response['tracks'].keys())
    # print(response['tracks']['items'])
    # print(len(response['tracks']['items']))
    # print(len(response['tracks']['items'][0].keys()))
    # print(response['tracks']['items'][0]['track']['external_urls']['spotify'])

    # Get links to all of the songs in this playlist
    song_links = [song['track']['external_urls']['spotify']
                  for song in response['tracks']['items']]

    return song_links


if __name__ == '__main__':
    print(get_top_50_links())
