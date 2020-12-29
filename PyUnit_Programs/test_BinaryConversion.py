# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:31:53
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:44

import unittest
import BinaryConversion

class BinaryConversionTest(unittest.TestCase):

    def test_decToBinary(self):
        assert(BinaryConversion.decToBinary(16) == "10000")
        

if __name__ == '__main__':
    unittest.main()