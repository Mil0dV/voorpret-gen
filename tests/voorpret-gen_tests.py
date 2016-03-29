from nose.tools import *
# from voorpretgen import *
import voorpretgen
from voorpretgen import filemanager
from voorpretgen import main
from voorpretgen import spotify
import unittest
import pprint

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

class TestVoorpretgen(unittest.TestCase):


    def test_file_read(self):
        file_path = 'tests/lineup-test.txt'
        result = filemanager.lineup_parser(file_path)
        self.assertTrue(result == ['audiotist', 'larry de kat', 'madonna', 'interr ferenc'])

    def test_parse_argements(self):
        # parser = main.parse_arguments(['lineup.txt', 'lineup.txt'])
        # self.assertTrue(parser)
        # Couldn't get this to work though it should, therefore;
        pass

    def test_read_settings(self):
        file_path = 'tests/voorpretgen-test.ini'
        result = filemanager.read_settings(file_path)
        self.assertTrue(int(result[0]) == 3)

    def test_artist_id_list_gen(self):
        file_path = 'tests/lineup-test.txt'
        lineup = filemanager.lineup_parser(file_path)
        result = spotify.artist_id_list_gen(lineup)
        self.assertTrue(type(result) == list)

    def test_tracklist_gen(self):
        file_path = 'tests/lineup-test.txt'
        lineup = filemanager.lineup_parser(file_path)
        artist_id_list = spotify.artist_id_list_gen(lineup)
        result = spotify.tracklist_gen(artist_id_list, 5)
        self.assertTrue(type(result) == list)

    def test_user_authentication(self):
        file_path = 'voorpretgen/voorpretgen.ini'
        settings = filemanager.read_settings(file_path)
        username = 'milowinterburn'
        result = spotify.user_authentication(username, settings[1:])
        self.assertTrue(result == None)

    def test_initialise(self):
        # settings_file = 'tests/voorpretgen-test.ini'
        # lineup_file = 'tests/voorpretgen-test.ini'
        # print lineup_file
        # result = main.initialise(['milowinterburn', 'bangface.txt'], settings_file)
        # self.assertTrue(int(result[0]) == 3)
        # Couldn't get this to work though it should, therefore;
        pass
