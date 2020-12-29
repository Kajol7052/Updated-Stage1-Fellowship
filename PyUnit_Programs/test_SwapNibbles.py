# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 22:25:07
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:49
import unittest
import SwapNibbles

class SwapNibblesTest(unittest.TestCase):

    def test_decTOBinary(self):
        self.assertEqual(SwapNibbles.decToBinary(100),70)



if __name__ == '__main__':
    unittest.main()