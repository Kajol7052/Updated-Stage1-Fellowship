# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 00:30:05
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:51

import unittest
import VendingMachine

class VendingMachineTest(unittest.TestCase):

    def test_countCurrency(self):
        assert(VendingMachine.countCurrency(16) == "10:1,5:1,1:1,")
        

if __name__ == '__main__':
    unittest.main()