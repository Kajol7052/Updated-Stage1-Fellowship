# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 21:24:51
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:50


import unittest
import TempCoversion

class TempConversionTest(unittest.TestCase):

    def test_convert_f(self):
        self.assertEqual(TempCoversion.convert_f(25),77)
        
    def test_convert_c(self):
        self.assertEqual(TempCoversion.convert_c(32),0)
        

if __name__ == '__main__':
    unittest.main()