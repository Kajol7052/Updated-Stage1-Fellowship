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

    def test_to_see_square_root_works_ok(self):
            self.assertEqual(2, self.calc.sqrt(4))
            self.assertEqual(4, self.calc.sqrt(16))


if __name__ == '__main__':
    unittest.main()