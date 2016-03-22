from nose.tools import *
# from voorpretgen import *
import voorpretgen
from voorpretgen import filemanager
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
        result = filemanager.readlines(file_path)
        self.assertTrue(len(result) == 2)
