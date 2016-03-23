import argparse
import sys

def parse_arguments(args):
  parser = argparse.ArgumentParser(
    description='Voorpret-gen - spotify playlist generator based on lineup',
    usage='voorpretgen [options] lineup_file')
  parser.add_argument('lineup_file', help='File with one artist per line')
  parser.add_argument('-n', metavar='top X tracks', help='Number of tracks to add to playlist')
  parser.add_argument('-p', metavar='playlist', help='Playlist name (default = lineup filename)')

  args = parser.parse_args()
  lineup_file = args.lineup_file
  top_x_tracks = args.n
  playlist_name = args.p

  return lineup_file, top_x_tracks, playlist_name


def main(args):
    print parse_arguments(args)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
