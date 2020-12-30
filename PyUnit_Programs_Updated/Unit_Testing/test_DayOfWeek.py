# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 21:49:25
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:45


import DayOfWeek
import unittest

class DayOfWeekTest(unittest.TestCase):

    def test_positive_day_of_week(self):
        self.assertEqual(DayOfWeek.day_of_week(12,28,2020),"Monday")
        self.assertEqual(DayOfWeek.day_of_week(12,29,2020),"Tuesday")
        self.assertEqual(DayOfWeek.day_of_week(12,30,2020),"Wednesday")
        self.assertEqual(DayOfWeek.day_of_week(12,31,2020),"Thursday")
        self.assertEqual(DayOfWeek.day_of_week(12,27,2020),"Sunday")
        self.assertEqual(DayOfWeek.day_of_week(12,26,2020),"Saturday")
        self.assertEqual(DayOfWeek.day_of_week(12,25,2020),"Friday")

    def test_negative_day_of_week(self):
        self.assertEqual(DayOfWeek.day_of_week(4,28,2021),"Friday")
        self.assertEqual(DayOfWeek.day_of_week(6,15,2020),"Tuesday")
    


if __name__ == "__main__":
    unittest.main()
