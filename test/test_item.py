#!/usr/bin/python3
# -*- coding: utf-8 -*-

# http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-1/



# http://sametmax.com/se-simplifier-les-tests-python-avec-pytest/

from __future__ import print_function, unicode_literals, division

import unittest
import operator
from item import Item



class TestItem(unittest.TestCase):

	def __init__(self):
		self.description = 'Salut, je suis une classe qui sert a tester les items'

	def test_get_description(self):
		item_a_tester = Item('Description Test')
		self.assertEqual(Item.get_description(self), 'Description Test')




        
        
if __name__ == '__main__':
    unittest.main()
