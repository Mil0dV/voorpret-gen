from nose.tools import *
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


    # def setUp(self):
    #     self.file = voorpretgen.file()

    def test_file_read(self):
        file_path = 'tests/lineup.txt'
        bla = filemanager.readlines(file_path)
        self.assertTrue(len(bla) == 2)
