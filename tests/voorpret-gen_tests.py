from nose.tools import *
import voorpretgen
import unittest
import pprint

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

class TestVoorpretgen(unittest.TestCase):

    file_path = 'tests/lineuptest.txt'

    def setUp(self):
        self.file = voorpretgen.file()

    def test_file_read(self):
        file = self.file.readlines(self.file_path)
        self.assertTrue(file['count'] == 2)
