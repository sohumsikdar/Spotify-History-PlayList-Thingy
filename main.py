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

    # check for errors in the response
    if(respose.status_code != 200):
        return None

    item = resp_json['item']
    # store the given information in a dictionary
    # if key error just return None
    current_track_info = {
        'artist': item['artists'][0]['name'],
        'track': item['name'],
        'id': item['id'],
        'duration': item['duration_ms']
    }
    
    return current_track_info

# update the number of times the track has been played
# host a csv on github gist and update the csv
def update_track_play_count(track_id, play_count):
    pass

def init_csv():
    pass

def main():
    # have a current track info variable for the previous track
    # and a current track info variable for the current track
    # if the current track info is different from the previous track info
    # update the number of times the track has been played - using duration of the track
    # and the number of times the track returned from the API is the same as the prev
    
    prev_track_info = None
    prev_track_play_time = 0
    init_csv()

    while True:
        current_track_info = get_current_track(cred.SPOTIFY_ACCESS_TOKEN)
        if(current_track_info is None):
            pass
        elif prev_track_info is None:
            prev_track_info = current_track_info
            prev_track_play_time += 5
        else:
            if prev_track_info['id'] == current_track_info['id']:
                prev_track_play_time += 5
            else:
                print(f"{prev_track_info['track']} has been played for {prev_track_play_time} seconds")
                prev_track_play_count = prev_track_play_time / (prev_track_info['duration'] / 1000)
                update_track_play_count(prev_track_info['id'], prev_track_play_count)
                prev_track_info = current_track_info
                prev_track_play_time = 0

        time.sleep(5)

if __name__ == '__main__':
    main()