#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:08:56 2024

@author: bing
"""


def max_profit(prices):
    # input your code here
    # Using 1 loop
    p = []
    for i in range(0, len(prices)-1):
        p.append(max(prices[i+1:])-prices[i])

    return max(p)


''' 
def max_profit(prices):
    # Using nested loops
    p = []
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            p.append(prices[j]-prices[i])

    return max(p)
'''


if __name__ == "__main__":

    prices = [800, 300, 600, 200, 100]
    # print(max_profit(prices))
    print(max_profit(prices))

    prices = [800, 300, 200, 100, 0]
    # print(max_profit(prices))
    print(max_profit(prices))
