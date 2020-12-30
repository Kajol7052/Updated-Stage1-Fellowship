# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 22:28:48
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:48
import unittest
import SquareRoot

class SquareRootTest(unittest.TestCase):

    def setUp(self):
            self.calc = SquareRoot.SquareRooter()

    def test_positive_sqrt(self):
            self.assertEqual(2, self.calc.sqrt(4))
            self.assertEqual(12, self.calc.sqrt(144))


    def test_negative_sqrt(self):
            self.assertEqual(5, self.calc.sqrt(10))
            self.assertEqual(12, self.calc.sqrt(320))
            

if __name__ == '__main__':
    unittest.main()