# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:50
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:38

import CustomExceptions


# function to print the day of week
def day_of_week(m, d, y):
    years = int((y - (14 - m)) / 12)
    l_years = int(years + (years/4) - (years/100) + (years/400))
    months = m + 12 * ((14 - m) / 12) - 2
    day = (d + l_years + 31*months / 12) % 7
    return choose_day(day)
    

 # function to choose day   
def choose_day(day):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    print (switcher.get(day, "Invalid day!"))
    return switcher.get(day, "Invalid day!")

if __name__ == "__main__":
    try:
        m = int(input("Enter month: "))
        d = int(input("Enter date: "))
        y = int(input("Enter year: "))
        if(m <= 0 or m > 12 or d <= 0 or d > 31 or y <= 0):
            raise CustomExceptions.ValueOutOfBoundError()
        day_of_week(m, d, y)
    except CustomExceptions.ValueOutOfBoundError:
        print("Value must be in given range! ")