import sys
import spotipy
import spotipy.util as util

def user_authentication(settings):
    print settings
    return 1


def artist_id_list_gen(artist_list):
    # expects artists as strings in a list
    # returns list of id's as unicode strings and internally keeps track of search failures

    def get_artist_id(name):
        # expects artist name as string
        # returns the associated ID as unicode, if no spotipy search result returns input name
        i = 0
        l = 1
        spotify = spotipy.Spotify()
        # search for artist in spotipy, and assign first result to results
        results = spotify.search(q= 'artist:'+ name, limit = l, offset = i, type='artist')

        try:
            # search for id in results
            return results[u'artists'][u'items'][0][u'id']
        except IndexError:
            # if no results return 0
            return name

    # append ID id_list or name in search_failure list
    artist_id_list = []
    artis_fail_search_list = []
    for name in artist_list:
        x = get_artist_id(name)
        if type(x) == unicode:
            artist_id_list.append(x)
        else:
            artis_fail_search_list.append(name)

    return artist_id_list

def tracklist_gen(artist_id_list, n):
    # expects list of artist id's and an integer for how many tracks per artists, maximum == 10!
    # returns a list of top track id's
    country_code = 'NL'
    spotify = spotipy.Spotify()
    top_tracks = []
    # for each artist id, get the top track search results
    for artist_id in artist_id_list:
        top_tracks.append(spotify.artist_top_tracks(artist_id, country=country_code))

    # for each top track search result, get all the track id's within and append them
    top_track_ids = []
    for x in top_tracks:
        count = 0
        for x in x[u'tracks']:
            count += 1
            if count <= n:
                top_track_ids.append(x[u'id'])
    # print spotify.track(top_track_ids[0])
    # print spotify.track(top_track_ids[5])
    # print top_track_ids
    # print 'len =' , len(top_track_ids)
    return top_track_ids
    # return 0

def write_playlist(track_id_list):
    pass
