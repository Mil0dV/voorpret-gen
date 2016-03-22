from nose.tools import *
from voorpretgen import file
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
        file_path = 'tests/lineup.txt'
        x = file.readlines(file_path)
        print len(x)
        self.assertTrue(len(x) == 2)
