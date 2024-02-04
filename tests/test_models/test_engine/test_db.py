#!/usr/bin/python3

"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""
import os
import unittest


@unittest.skipIf(
	os.getenv('HBNB_TYPE_STORAGE') != 'db', 'Invalid storage type')
class TestDBStorageDocs(unittest.TestCase):
	""" Class to test the database storage method """
	pass
