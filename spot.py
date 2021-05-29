import json
import time
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

client_id = '8be5f0367b7a4b54b730b33faa7c1b2c'
client_secret = '0bc78da67fa44fe985c2586aa74d7e1d'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)


#func to extract all track ids

def get_track_ids(playlist_id):
    music_id_list = []
    playlist = sp.playlist(playlist_id)

    for item in playlist['tracks']['items']:
        music_track = item['track']
        music_id_list.append(music_track['id'])
    return music_id_list

#function to extract all details of track

def get_track_data(track_id):
    meta = sp.track(track_id)

    track_details = {'name':meta['name'], 'album':meta['album']['name'], 
                        'artist':meta['album']['artists'][0]['name'], 'release_date': meta['album']['release_date'],
                        'duration_in_mins':round((meta['duration_ms']*0.001)/60, 2)}
    return track_details

#get the ids for all songs

playlist_id = input('Enter the playlist id')
track_ids = get_track_ids(playlist_id)
print(len(track_ids))

print(track_ids)

tracks = []

for i in range(len(track_ids)):
    time.sleep(.5)
    track = get_track_data(track_ids[i])
    tracks.append(track)

with open('spotify_data.json', 'w') as outfile:
    json.dump(tracks, outfile, indent= 4)




