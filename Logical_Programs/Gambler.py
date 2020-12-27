"""
   * author - kajol
   * date - 12/25/2020
   * time - 10:29 AM
   * package - com.bridgelabz.logicalprograms
   * Title - Gambler program to print number of wins and percentage of win and loss.
"""

import random


class GamblerSimulation:
    def gambler(self, stake, goal):
        """
        :param stake: initial amaount
        :param goal: goal to reach particular amount
        :return: win or loss
        """
        try:
            play = int(input("Enter no. of times you want to play : "))
            if play <= 0 or play >= 51:
                print("Enter number between 1 and 50")
                exit(1)
            dice = int(input("Which number on the dice you want to bet : "))
            if dice <= 0 or dice >= 7:
                print("Enter between 1 and 6")
                exit(1)
            win = 0
            loss = 0

            for i in range(play):
                amount = stake
                while goal > amount > 0:
                    rand = random.randint(1, 6)  # randomly generating dice number
                    if rand == dice:
                        amount = amount + 1
                        win += 1
                    else:
                        amount = amount - 1
                        loss += 1

                print("Total amount won is ", amount)
            print("Number of wins are ", win, "and Number of loss are ", loss)
            print("% of wins are ", win/(win+loss), "and % of loss are ", loss/(win+loss))
        except ValueError:
            print("check the input ")


if __name__ == '__main__':
    try:
        stake = int(input("Stake: "))
        goal = int(input("Goal: "))
        if stake <= 0 or stake >= 1000:
            print("Enter the stake between 0 and 1000")
            if goal <= 0 or goal >= 1000:
                print("Enter the goal between 0 and 1000")
        caller = GamblerSimulation()
        caller.gambler(stake, goal)
    except ValueError:
        print("Enter valid input")
