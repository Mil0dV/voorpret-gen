import argparse
import sys
from filemanager import *
from spotify import *

def parse_arguments(args):
    parser = argparse.ArgumentParser(
        description='Voorpret-gen - spotify playlist generator based on lineup',
        usage='voorpretgen [options] username lineup_file')
    parser.add_argument('username', help='Spotify username')
    parser.add_argument('lineup_file', help='File with one artist per line')
    parser.add_argument('-n', metavar='top X tracks', help='Number of tracks to add to playlist')
    parser.add_argument('-p', metavar='playlist', help='Playlist name (default = lineup filename)')

    args = parser.parse_args()
    lineup_file = args.lineup_file
    username = args.username
    top_x_tracks = args.n
    playlist_name = args.p

    return lineup_file, top_x_tracks, playlist_name, username

def initialise(args, settings_file):
    arguments = parse_arguments(args)
    username = arguments[3]
    top_x_set, client_id, client_secret, redirect_uri = read_settings(settings_file)
    spot_token = get_token(username, client_id, client_secret, redirect_uri)
    top_x_tracks = arguments[1] if arguments[1] else int(top_x_set)
    lineup = lineup_parser(arguments[0])
    playlist_name = arguments[2]
    return lineup, top_x_tracks, playlist_name

def main(args):
    settings_file = 'voorpretgen/voorpretgen.ini'
    lineup, top_x_tracks, playlist_name = initialise(args, settings_file)
    artist_ids = artist_id_list_gen(lineup)
    top_x_tracks = 3
    track_id_list = tracklist_gen(artist_ids, top_x_tracks)
    write_playlist(track_id_list, playlist_name)
    print 'track_id_list= ',
    print track_id_list

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
