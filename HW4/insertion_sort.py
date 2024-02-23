#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:22:57 2024

@author: bing
"""
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        v = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > v:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = v


if __name__ == "__main__":
    start = timeit.default_timer()
    
    lst = [ 10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    insertion_sort(lst)
    print(lst)
    
    stop = timeit.default_timer()
    
    print("Time for Insertion Sort:",stop-start)
    
    lst = [ 0, 1, 2, 3]
    insertion_sort(lst)
    print(lst)
    
    