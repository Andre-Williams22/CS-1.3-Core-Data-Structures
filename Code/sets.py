#from hashtable import HashTable
from binarytree import BinarySearchTree


class Treeset:
    def __init__(self, elements=None):
        ''' initialize a new empty set structure, and add each element if a sequence is given '''
        #self.hash = HashTable()
        self.tree = BinarySearchTree()
        self.size = 0 
        if items is not None:
            for item in items:
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
            raise ValueError(f'Cannot add element to set again: {}'.format(element))
        else:
            self.tree.insert(element)
            self.size += 1


    def remove(self,element):
        '''remove element from this set, if present, or else raise KeyError '''
        if self.tree.contains(element):
            self.tree.delete(element)
            self.size -= 1 
        else:
            raise ValueError(f'Element is not in the set: {}'.format(element))

    def union(self,other_set):
        '''return a new set that is the union of this set and other_set'''
        new_set = Set()
        for element in self.tree.items_in_order():
            if element in self.tree.items_in_order and element in other_set:
                new_set.add(element)
        return new_set 
        

    def intersection(self,other_set):
        '''return a new set that is the intersection of this set and other_set  '''
        new_set = Set()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                new_set.add(element)
        return new_set 


    def difference(self,other_set):
        '''return a new set that is the difference of this set and other_set '''

    def is_subset(other_set):
        '''return a boolean indicating whether other_set is a subset of this set'''