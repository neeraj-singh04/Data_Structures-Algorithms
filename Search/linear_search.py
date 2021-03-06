# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:49:41 2019

@author: neerajkumar65
"""

def linear_search(seq,target):
    """Pure implementation of linear search algorithm in Python
    :param sequence: some sorted collection with comparable items
    :param target: item value to search
    :return: index of found item or None if item is not found
    
    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> linear_search([0, 5, 7, 10, 15], 6)
    """
    
    for index , item in enumerate(seq):
        if item == target:
            return index
    return None

if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    seq = [int(item) for item in user_input.split(",")]
    
    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result =linear_search(seq,target)
    if result is not None:
        print(f"{target} found at position : {result}")
    else:
        print("Not Found")
        
    
