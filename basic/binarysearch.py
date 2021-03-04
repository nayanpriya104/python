"""
Binary Search Algorithm
------------
"""

# iterative implementation of binary search in python

def binary_search(a_list, item):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.
    a_list -- sorted list of inetgers
    item -- integer you are searching for the position of
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        i = int((first+last)/2)
        if a_list[i] == item:
            return '{} found at position {}'.format(item,i)
        elif a_list[i] > item:
            last = i-1
        elif a_list[i] < item:
            first = i+1
        else:
            return ' not found in the list'.format(item=item)

# recursive implementationof binary search in Python

def binary_search_recursive(a_list, item):
    """Performs recursive binary search of an integer in a given,sorted, list.
    a_list -- sorted list of integers
    item -- inetger you are searching for the position of
    """

    first = 0
    last == len(a_list) - 1
    if len(a_list) == 0:
        return '{} was not found in the list'.format(item)
    else:
        i = int(first+last)/2
        if item == a_list[i]:
            return 'found {}'.format(item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:],item)
            else:
                return binary_search_recursive(a_list[:i],item)
    
    
