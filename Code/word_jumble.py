# import os
from itertools import permutations 
from sets import Treeset 
from hashtable import HashTable
from linkedlist import LinkedList

# hashtable = {}

def open_file(length):
    ''' Return words that are length of input word''' 
    with open("/usr/share/dict/words", 'r') as fd:
        for line in fd:
            line = line.strip()

    # Returns set of words in length 
    return Treeset([word for word in fd if len(word) == length])


def reconfigure(word):
    '''Returns the items in common in a string from the two sets '''
    anagrams = list(permutations(word))
    # convert this to a list of str, not tuple
    anagrams = [''.join(list(word)) for word in anagrams]
    # convert this to a Set
    anagrams = Treeset(anagrams)
    # generate the set of all English words in the dictionary file
    actual_words = open_file(len(word))
    # find the intersection between the two
    overlap = anagrams.intersection(actual_words)
    # dump all the words into a LinkedList, and return the head
    unscrambled_words = LinkedList(word for word in overlap.collection.keys())
    if unscrambled_words.head is not None:
        return unscrambled_words.head.data
    else:
        return 'Word Does not exist'

# print(hashtable)

# # Function to find permutations of a given string 
# def allPermutations(str): 
#      # Get all permutations of string 'ABC' 
#      permList = permutations(str) 
  
#      # print all permutations 
#      for perm in list(permList): 
#          print (''.join(perm)) 
        
# #print(allPermutations())


import pprint
from collections import deque

pp = pprint.PrettyPrinter(indent=4)

# inp = raw_input("Enter a sentence to show as trie\n")
# words = inp.split(" ")
trie = {}


def trie_recursion(trie_ds, word):
    try:
        letter = word.popleft()
        out = trie_recursion(trie_ds.get(letter, {}), word)
    except IndexError:
        # End of the word
        return {}

    # Dont update if letter already present
    if not trie_ds.has_key(letter):
        trie_ds[letter] = out

    return trie_ds

for word in line:
    # Go through each word
    trie = trie_recursion(trie, deque(word))

pprint.pprint(trie)


if __name__ == 'main':
    pass 