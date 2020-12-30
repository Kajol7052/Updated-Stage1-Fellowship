# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 22:25:07
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:49
import unittest
import SwapNibbles

class SwapNibblesTest(unittest.TestCase):

    def test_positive_decTOBinary(self):
        self.assertEqual(SwapNibbles.decToBinary(100),70)
        self.assertEqual(SwapNibbles.decToBinary(50),35)
        
    def test_negative_decTOBinary(self):
        self.assertEqual(SwapNibbles.decToBinary(75),70)
        self.assertEqual(SwapNibbles.decToBinary(85),40)
        
    


if __name__ == '__main__':
    unittest.main()