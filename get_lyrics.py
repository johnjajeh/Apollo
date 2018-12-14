#! /usr/bin/env python
import sys
import os

from directory_util import make_artist_directory, store_lyrics_in_file
from lyric_util import collect_artist_song


"""
Load song data for artist using genius API
    - try to read the artist name from command line params
    - use that to query Genius API
    - display results to see data schema
Create directory structure for storing lyric data
    - in current working directory (not directory of source)
        create a directory for the artist
    - for each of the songs, save the lyrics into a file with name of song
"""

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Unable to read artist name from cli args')
    print(sys.argv[1])

    artist = sys.argv[1]
    make_artist_directory(artist)
    count = None if len(sys.argv) < 3 else int(sys.argv[2])
    songs = collect_artist_song(artist, count)
    for song_data in songs:
        store_lyrics_in_file(*song_data)
