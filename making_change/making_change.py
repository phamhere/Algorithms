#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # base cases
    if amount < 5:
        return 1
    elif amount < 10:
        return 2
    elif amount < 15:
        return 4
    elif amount < 20:
        return 6
    elif amount < 25:
        return 9
    elif amount < 30:
        return 13
    elif amount < 35:
        return 18

    return making_change()


# n(0) = 1
# n(1) = 1
# n(5) = 2
# n(10) = 4
# n(15) = 6
# n(20) = [1*20][1*15,5][1*10,5*2][1*5,5*3][5*4][1*10,10][10*2][5*2,10][1*5,5,10] so 9
# n(25) = [[1*25],[1*20,5],[1*15,5*2],[1*10,5*3],[1*5,5*4],[5*5],[1*15,10],[1*5,10*2],[25],[5*3,10],[5,10*2],[1*10,5,10],[1*5,5*2,10]] so 13
# n(30) = 18

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
