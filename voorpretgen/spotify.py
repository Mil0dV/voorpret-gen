import sys
import spotipy
import spotipy.util as util

# commented out, it breaks all tests when sys.exit()

# scope = 'user-library-read'
#
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
# #     print "Usage: %s username" % (sys.argv[0],)
#     sys.exit()
#
# token = util.prompt_for_user_token(username, scope)
#
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print track['name'] + ' - ' + track['artists'][0]['name']
# else:
#     print "Can't get token for", username

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

def top_tracklist_gen(artist_id_list)
    # artist_top_tracks(artist_id, country='US')
    pass

def write_playlist(track_id_list):
    pass
