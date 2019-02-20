#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # setting a starting max_profit to compare against
    max_profit = prices[1] - prices[0]
    # looping through prices
    for i in range(len(prices)):
        """looping through prices for each price, starting at i to not
        going backwards since need to buy first"""
        for j in range(i, len(prices) - 1):
            """comparing the profit of j+1 since don't want to compare
            same values incase profit is negative"""
            if prices[j + 1] - prices[i] > max_profit:
                max_profit = prices[j + 1] - prices[i]
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
