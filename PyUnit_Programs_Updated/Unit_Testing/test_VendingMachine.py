# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 00:30:05
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:51

import unittest
import VendingMachine

class VendingMachineTest(unittest.TestCase):

    def test_positive_countCurrency(self):
        assert(VendingMachine.countCurrency(16) == "10:1,5:1,1:1,")
        assert(VendingMachine.countCurrency(729) == "500:1,200:1,20:1,5:1,2:2,")
        assert(VendingMachine.countCurrency(2765) == "2000:1,500:1,200:1,50:1,10:1,5:1,")
        
    
    def test_negative_countCurrency(self):
        assert(VendingMachine.countCurrency(15) == "10:2,5:1,")
        assert(VendingMachine.countCurrency(116) == "100:2,5:1,1:1,")
        assert(VendingMachine.countCurrency(2500) == "2000:1,5:1,1:1,")
            

if __name__ == '__main__':
    unittest.main()