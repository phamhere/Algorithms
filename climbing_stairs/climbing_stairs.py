#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)


"""after doing some calculations for simple n's, I see a pattern where it's
the last three n() values added together"""
# n(1) = 1
# n(2) = 2
# n(3) = 4
# n(4) = [3,1][1,3][2,2][1,1,1,1][1,1,2][2,1,1][1,2,1] so 7
# n(5) = [1,1,1,1,1][1,1,1,2][1,1,2,1][1,2,1,1][2,1,1,1][1,2,2][2,1,2][2,2,1][1,1,3][1,3,1][3,1,1][2,3][3,2] so 13
# n(6) = [[1,1,1,1,1,1],[1,1,1,1,2],[1,1,1,2,1],[1,1,2,1,1],[1,2,1,1,1],[2,1,1,1,1],[1,1,2,2],[1,2,2,1],[2,2,1,1],[1,2,1,2],[2,1,2,1],[2,1,1,2],[2,2,2],[1,1,1,3],[1,1,3,1],[1,3,1,1],[3,1,1,1],[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2],[3,3]] so 24

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
