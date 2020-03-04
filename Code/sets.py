#!python
#from hashtable import HashTable
from binarytree import BinarySearchTree, BinaryTreeNode

class Treeset:
    def __init__(self, elements=None):
        ''' initialize a new empty set structure, and add each element if a sequence is given '''
        #self.hash = HashTable()
        self.tree = BinarySearchTree()
        self.element = BinaryTreeNode()
        self.size = 0 
        if elements is not None:
            for item in elements:
                self.insert(item)


    def size(self):
        '''property that tracks the number of elements in constant time 
        Average Case Runtime: O(1) because we're updating the size variable after each deletion and addition to an element'''
        return self.size 


    def contains(self,element):
        ''' return a boolean indicating whether element is in this set 
        Average Case Runtime: O(log(n)) because we're searching the binary search tree'''
        return self.tree.contains(element)


    def add(self,element):
        ''' add element to this set, if not present already 
        Average case Runtime: O(log (n)) Because we must apply binary search to add an element '''
        if self.tree.contains(element):
            raise ValueError(f'Cannot add element to set again: {element}')
        else:
            self.tree.insert(element)
            self.size += 1


    def remove(self,element):
        '''remove element from this set, if present, or else raise KeyError
        Average case Runtime: O(log (n))  Because we perform binary search to find the item to delete'''
        if self.tree.contains(element):
            self.tree.delete(element)
            self.size -= 1 
        else:
            raise ValueError(f'Element is not in the set: {element}')

    def union(self,other_set):
        '''return a new set that is the union of this set and other_set
        Runtime: (m + n) * log(m) because we add the length of each set to the time of the add function calls '''
        new_set = Treeset()
        for element in self.tree.items_pre_order(): #O(log(m)) # pre-order will generate the exact same tree every time 
            new_set.add(element)

        for element in self.tree.items_pre_order(): # pre-order will generate the exact same tree every time
            if not new_set.contains(element): #O(log(m))
                new_set.add(element)
        return new_set 
        

    def intersection(self,other_set):
        '''return a new set that is the intersection of this set and other_set  
        Average Case Runtime: O(n) '''

        new_set = Treeset()
        for element in self.tree.items_pre_order():
            if other_set.contains(element):
                new_set.add(element)
        return new_set 


    def difference(self,other_set):
        '''return a new set that is the difference of this set and other_set 
        Average Case Runtime: O(n) because we have to check all the nodes to see if in the other set.'''
        # make a new empty set
        new_set = Treeset()
        # iterate over each item in the self set 
        for element in self.tree.items_pre_order:
        # if the item is not in other set then add to the new set
            if element not in other_set.contains():
                new_set.add(element)
        # return the new set
        return new_set 


    def is_subset(self, other_set):
        '''return a boolean indicating whether other_set is a subset of this set
        Best Case: O(1) if the size is of other_set is bigger then we return False
        Average Case Runtime: O(log(n)) if we traverse through all the nodes. In the smaller set. '''
        if len(self) > len(other_set): 
            return False
        for item in self.tree.items_pre_order():
            if not other_set.contains(item):
                # found an item not in the two sets
                return False
        return True