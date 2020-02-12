#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        #TODO: Check if empty
        if self.list.head is None:
            return True
        else:
            return False
        #return self.list.head is None

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? [TODO]"""
        # TODO: Push given item
        # if self.is_empty() is True:
        #     return None

        return self.list.prepend(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        
        if self.list.is_empty():
            return None 
        return self.list.head.data # looks at end of ll which is top of stack and grabs the tail.

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty() is True:
            raise ValueError('List is empty: {}'.format(self.list))
        temp_node = self.list.head.data
        print("top of stack: ", temp_node)
        self.list.delete(temp_node)
        return temp_node
       




# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False 

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        count = 0
        for item in self.list:
            count += 1
        return count 

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? [TODO]"""
        # TODO: Insert given item
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if len(self.list) != 0:
            return self.list[-1] # return index
        else:
            return None 

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty() is True:
            raise ValueError('List is empty: {}'.format(self.list))
        else:
            top = self.list.pop()
            return top

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
#Stack = ArrayStack
