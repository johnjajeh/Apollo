#! /usr/bin/env python3
import os
import re
import string
import sys


def make_valid_filename(name):
    valid_chars = r'\W+'
    valid_name = re.sub(valid_chars, '', name)
    print(valid_name)
    return valid_name

def make_artist_directory(artist):
    artist = make_valid_filename(artist)
    if not isinstance(artist, str):
        artist = str(artist)

    try:
        os.mkdir(artist)
    except Exception as e:
        raise e

def store_lyrics_in_file(artist, song, lyrics):
    path = os.path.join(
            make_valid_filename(artist),
            make_valid_filename(song)
        )
    with open(path, 'w') as f:
        f.writelines(lyrics)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise Exception('Unable to read artist, song, and lyrics from command line\n'
                        'Please enter those in order as arguments')
    print('testing make artist directory:')
    _, artist, song, lyrics = sys.argv

    artist = make_valid_filename(artist)
    song = make_valid_filename(song)
    
    make_artist_directory(artist)
    print('Artist directory was created: {}'.format(
            os.path.isdir(artist)
        ))
    try:
        os.rmdir(artist)
    except Exception as e:
        print('unable to create artist directory and delete it')

    make_artist_directory(artist)
    store_lyrics_in_file(artist, song, lyrics)
    print('Artist song file created: {}'.format(
            os.path.exists(os.path.join(artist, song))
        ))
    with open(os.path.join(artist, song), 'r') as f:
        print('File written contains artist lyrics: {}'.format(
                f.readlines() == lyrics
            ))
    try:
        os.rmdir(artist)
    except Exception as e:
        print('unable to store artist song as file and delete it')

