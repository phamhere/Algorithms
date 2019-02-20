#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    output = []
    plays = ['rock', 'paper', 'scissors']

    # using a helper recursion method since need to return a list
    def helper_method(m, lst):
        # base case
        if m == 0:
            output.append(lst)
            return

        # looping through plays to insert it into array
        for play in plays:
            # making a newlist since don't want to reference old one
            newlst = lst[:]
            newlst.append(play)
            helper_method(m-1, newlst)

    # calling helper method with n and empty arr to work with
    helper_method(n, [])

    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
