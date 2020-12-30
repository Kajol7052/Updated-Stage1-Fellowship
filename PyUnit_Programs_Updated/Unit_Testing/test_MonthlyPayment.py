# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 21:35:04
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:46



import unittest
import MonthlyPayment

class MonthlyPaymentTest(unittest.TestCase):

    def test_positive_monthly_payment(self):
        self.assertEqual(MonthlyPayment.monthly_payment(100,2,20),5.09)
        self.assertEqual(MonthlyPayment.monthly_payment(2000,4,15),55.66)
        
    
    def test_negative_monthly_payment(self):
        self.assertEqual(MonthlyPayment.monthly_payment(1200,2,20),12.00)
            

if __name__ == '__main__':
    unittest.main()