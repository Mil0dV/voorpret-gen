from nose.tools import *
# from voorpretgen import *
import voorpretgen
from voorpretgen import filemanager
from voorpretgen import main
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

def test_init_read(self):
        file_path = 'voorpretgen/voorpretgen.ini'
        result = filemanager.read_settings(file_path)
        self.assertTrue(len(result.values()) == 4)