#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import re

import deliverable as student

class PE1_5(unittest.TestCase):

    def setUp(self):
        self.covername = 'sample.pgm'
        self.coverheader = ['P2','5','5','255']
        self.coverpixels = [
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250',
            '250','250','250','250','250'
        ]
        self.coverdata = '\n'.join([str(c) for c in self.coverheader+self.coverpixels])

        self.stegname = 'steg.pgm'
        self.stegheader = ['P2','5','5','255']
        self.stegpixels = [
            '250','251','251','250','250',
            '250','250','251','250','251',
            '251','251','250','251','250',
            '250','251','250','250','250',
            '250','250','250','250','250'
        ]
        self.stegdata = '\n'.join([str(c) for c in self.stegheader+self.stegpixels])

        self.msg = 'at'

    def test_decode_pgm(self):
        fp = io.StringIO(self.stegdata)
        with unittest.mock.patch('builtins.open',return_value=fp):
            answered = student.decode_pgm(self.stegname)
            self.assertEqual(answered,self.msg)

    def test_encode_pgm(self):
        coverfp = io.StringIO(self.coverdata)
        stegfp = io.StringIO()
        mockfileobj = unittest.mock.MagicMock(wraps=stegfp)
        mockfileobj.__enter__.return_value = mockfileobj
        mockfileobj.close.return_value = None
        
        def side_effect(filename,mode='r',**kwargs):
            if filename == self.stegname:
                return mockfileobj
            elif filename == self.covername:
                return coverfp
            else:
                raise FileNotFoundError

        with unittest.mock.patch('builtins.open',side_effect=side_effect) as m:
            student.encode_pgm(self.msg,self.covername,self.stegname)
            
            answered = stegfp.getvalue()
            answered = answered.split()

            self.assertEqual(answered[:4],self.stegheader)
            self.assertEqual(answered[4:],self.stegpixels)

if __name__ == '__main__':
    unittest.main()
