#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import List, Union


def sum_mixed_list(imput_list: List[Union[int; float]]) -> float:
    '''
     function sum_mixed_list which takes a list mxd_lst of int and floats as
     argument and returns their sum as a float
    '''

    return sum(imput_list)
