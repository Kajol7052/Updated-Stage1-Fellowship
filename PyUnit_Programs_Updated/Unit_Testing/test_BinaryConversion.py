# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:31:53
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:44

import unittest
import BinaryConversion

class BinaryConversionTest(unittest.TestCase):

    def test_positive_decToBinary(self):
        assert(BinaryConversion.decToBinary(16) == "10000")
        assert(BinaryConversion.decToBinary(106) == "1101010")
        assert(BinaryConversion.decToBinary(12) == "1100")

    def test_negative_decToBinary(self):
        assert(BinaryConversion.decToBinary(15) == "1100")
        assert(BinaryConversion.decToBinary(102) == "1011000")
    
        
        

if __name__ == '__main__':
    unittest.main()