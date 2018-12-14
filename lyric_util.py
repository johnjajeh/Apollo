import lyricsgenius as genius
import os

api = genius.Genius(os.environ.get('GENIUS_API_TOKEN'))


# artist name, max songs to collect
# returns [
#     [
#        <artist>,
#        <song_tile>,
#        <lyrics>
#     ],
#     ...
#   ]
def collect_artist_song(artist, max_songs=None):
    artist_search = api.search_artist(artist, max_songs)
    


    return []




# how many songs


'''

~~ Pseudo Code ~~

input url of Genius musician?

check if url is valid for a musician?
    if true
        continue
    else
        raise Exception

store the artist's ID to have access to the songs
numOfSongs = store the number of songs by the artist

for i in range (numOfSongs)
    write lyrics into txt file in folder directory set (in directory_util.py)


~~~~~

raw_annotatable_url

https://github.com/johnwmillr/LyricsGenius/blob/master/lyricsgenius/artist.py
'''


