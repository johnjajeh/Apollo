import lyricsgenius as genius
import os
import re

api = genius.Genius(os.environ.get('GENIUS_API_TOKEN'))


'''
    Returns an list containing lists of (1) song 
    titles and (2) lyrics of a specified artist
'''
def collect_artist_songs(name, max_songs=None):
    artist = api.search_artist(name, max_songs=max_songs)

    songArray = []

    for song in artist.songs:
        songArray.append([song.title, clean_lyrics(song.lyrics)])

    return songArray

'''
    Returns pure lyrics from lyrics with metadata
'''
def clean_lyrics(lyrics):
    to_remove = r'\[[^]]+\]'
    return re.sub(to_remove, '', lyrics).strip()
