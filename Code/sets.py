#from hashtable import HashTable
from binarytree import BinarySearchTree


class Treeset:
    def __init__(self, elements=None):
        ''' initialize a new empty set structure, and add each element if a sequence is given '''
        #self.hash = HashTable()
        self.tree = BinarySearchTree()
        self.size = 0 
        if elements is not None:
            for item in elements:
                self.insert(item)


    def size(self):
        '''property that tracks the number of elements in constant time '''
        return self.size 


    def contains(self,element):
        ''' return a boolean indicating whether element is in this set '''
        return self.tree.contains(element)


    def add(self,element):
        ''' add element to this set, if not present already '''
        if self.tree.contains(element):
            raise ValueError(f'Cannot add element to set again: {element}')
        else:
            self.tree.insert(element)
            self.size += 1


    def remove(self,element):
        '''remove element from this set, if present, or else raise KeyError '''
        if self.tree.contains(element):
            self.tree.delete(element)
            self.size -= 1 
        else:
            raise ValueError(f'Element is not in the set: {element}')

    def union(self,other_set):
        '''return a new set that is the union of this set and other_set'''
        new_set = Treeset()
        for element in self.tree.items_pre_order(): #O(log(m)) # pre-order will generate the exact same tree every time 
            new_set.add(element)

        for element in self.tree.items_pre_order(): # pre-order will generate the exact same tree every time
            if not new_set.contains(element): #O(log(m))
                new_set.add(element)
        return new_set 
        

    def intersection(self,other_set):
        '''return a new set that is the intersection of this set and other_set  '''
        new_set = Treeset()
        for element in self.tree.items_pre_order():
            if other_set.contains(element):
                new_set.add(element)
        return new_set 


    def difference(self,other_set):
        '''return a new set that is the difference of this set and other_set '''
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
        '''return a boolean indicating whether other_set is a subset of this set'''
        if len(self) > len(other_set): 
            return False
        for item in self.tree.items_pre_order():
            if not other_set.contains(item):
                # found an item not in the two sets
                return False
        return True