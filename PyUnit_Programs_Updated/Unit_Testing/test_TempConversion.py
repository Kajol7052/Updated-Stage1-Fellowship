# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 21:24:51
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:50


import unittest
import TempCoversion

class TempConversionTest(unittest.TestCase):

    def test_positive_convert_f(self):
        self.assertEqual(TempCoversion.convert_f(25),77)
        self.assertEqual(TempCoversion.convert_f(38),100)
        
        
    def test_positive_convert_c(self):
        self.assertEqual(TempCoversion.convert_c(32),0)
        self.assertEqual(TempCoversion.convert_c(12),-11)
        
    def test_negative_convert_f(self):
        self.assertEqual(TempCoversion.convert_f(27),65)
        self.assertEqual(TempCoversion.convert_f(32),54)
        
        
    def test_negative_convert_c(self):
        self.assertEqual(TempCoversion.convert_c(15),0)
        self.assertEqual(TempCoversion.convert_c(45),6)

if __name__ == '__main__':
    unittest.main()