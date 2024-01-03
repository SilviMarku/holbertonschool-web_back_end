#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import List


def sum_list(imput_list: List[float]) -> float:
    '''
     function sum_list which takes a list imput_list of floats as
     argument and returns their sum as a float
    '''

    return sum(imput_list)
