try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Spotify playlist import/export/create tool',
    'author': 'Milo de Vries',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'milo@xdh.nl',
    'version': '0.1',
    'install_requires': ['nose, spotipy'],
    'packages': ['voorpretgen'],
    'scripts': [],
    'name': 'voorpretgen'
}

setup(**config)
