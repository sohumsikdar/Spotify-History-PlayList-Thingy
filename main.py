from pprint import pprint
import time
import cred
import requests

def get_current_track(access_token):
    respose = requests.get(
        cred.SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    )
    resp_json = respose.json()
    current_track_info = {
        'artist': resp_json['item']['artists'][0]['name'],
        'track': resp_json['item']['name'],
        'id': resp_json['item']['id'],
        'link': resp_json['item']['external_urls']['spotify']
    }
    return current_track_info


def main():
    while True:
        current_track_info = get_current_track(
            cred.SPOTIFY_ACCESS_TOKEN
        )
        pprint(current_track_info, indent=4)
        time.sleep(1)

if __name__ == '__main__':
    main()