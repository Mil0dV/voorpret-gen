Voorpret-gen - spotify playlist generator based on lineup

Setup:
- git clone
- python setup.py install (might need sudo)

usage: python voorpretgen/main.py [options] username lineup_file

positional arguments:
  username         Spotify username
  lineup_file      File with one artist per line

optional arguments:
  -h, --help       show this help message and exit
  -n top X tracks  Number of tracks to add to playlist
  -p playlist      Playlist name (default = lineup filename)
