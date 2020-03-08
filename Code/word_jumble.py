# import os
import sys
from itertools import permutations 
from sets import Treeset 
from stack import LinkedStack
from hashtable import HashTable
from linkedlist import LinkedList

# hashtable = {}

def open_file(length):
    ''' Return words that are length of input word''' 
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.read().split("\n")
    file.close()

    # Returns set of words in length 
    return Treeset([word for word in words_list if len(word) == length])

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


def solve_puzzle(jumbled_list):
    '''solves jumble by unscrambling a list of words '''
    # create a dictionary to store the words
    hashtable = HashTable(len(jumbled_list))
    
    jumbled_list = [reconfigure(word) for word in jumbled_list]

    for i in range(len(jumbled_list)):
        print(f"'{jumbled_list[i]}'--> '{jumbled_list[i]}'" )
        # store indices we're interested in at each solved word
    letters_of_interest = [
        jumbled_list[0][2] + jumbled_list[0][4],
        (jumbled_list[1][0] + jumbled_list[1][1] +
         jumbled_list[1][3]),
        jumbled_list[2][4],
        jumbled_list[3][3] + jumbled_list[3][4],
    ]

    solution = ''
    for letter in letters_of_interest:
        solution += letter
    return solution

# print(hashtable)

# # Function to find permutations of a given string 
# def allPermutations(str): 
#      # Get all permutations of string 'ABC' 
#      permList = permutations(str) 
  
#      # print all permutations 
#      for perm in list(permList): 
#          print (''.join(perm)) 
        
# #print(allPermutations())

# def trie_recursion(trie_ds, word):
#     try:
#         letter = word.popleft()
#         out = trie_recursion(trie_ds.get(letter, {}), word)
#     except IndexError:
#         # End of the word
#         return {}

#     # Dont update if letter already present
#     if not trie_ds.has_key(letter):
#         trie_ds[letter] = out

#     return trie_ds

# for word in line:
#     # Go through each word
#     trie = trie_recursion(trie, deque(word))

# pprint.pprint(trie)


if __name__ == 'main':
    first_four = HashTable(4)
    jumbled = ['tefon','sokik','niumem','siconu']
    print(f'The answer to the jumble is: {solve_puzzle(jumbled)}')
