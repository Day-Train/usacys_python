#!/usr/bin/env python3
import unittest

import deliverable as student
#import solution as student

class OOPTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_card(self):
        if not 'Card' in dir(student):
            self.fail('class Card does not exist')


    def test_deck(self):
        if not 'Deck' in dir(student):
            self.fail('class Deck does not exist')
        else:
            if not 'shuffle' in dir(student.Deck):
                self.fail('method shuffle does not exist')
            if not 'deal' in dir(student.Deck):
                self.fail('method deal does not exist')

if __name__ == '__main__':
    unittest.main()

