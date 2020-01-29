#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array): # O(n)
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    for num in array: # O(n)
        if num == item: # O(1)
            return num # O(1)
        else:
            return linear_search_recursive(array, item, index+1) # O(1)
    return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left, right = 0, len(array)-1

    if len(array) == 0: # O(1)
        return None # O(1)

    while left <= right: # O(n)
        mid = left+(right-left)//2 # O(1)
        #print("mid: ", mid)
        if item == array[mid]: # O(1)
            return mid # returns an index of the item 
        elif item > array[mid]: # O(1)
            
            left = mid+1 # O(1)

        else:
           
            right = mid-1 # O(1)
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left is None and right is None: # O(1)
        left,right = 0, len(array)-1 # O(1)

    mid = left + (right - left) // 2 # O(1)
    #print("mid: ", mid)

    if left > right: # if search through entire list and didn't find item 
        return None 

    if array[mid] == item: # O(1)
        return mid # returns index of the item 
    elif item > array[mid]: # O(1)
        return binary_search_recursive(array, item, mid+1, right) # O(log(n))
    else:
        return binary_search_recursive(array, item, left, mid-1) # O(log(n))

    # return None 

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

#names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']

#print(binary_search(names, 'Alex'))