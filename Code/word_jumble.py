# Different Solutions:
# 1. Sorted array + Vinary search
# 2. Binary Search Tree
# 3. Permutations
# 4. Dictionary Lookups ==> word_jumble_sort.py
# 5. Sets
# 6. Combinations
# 7. Anagram Trie (Prefix Trie)

# import os
# import sys
# from itertools import permutations 
# from sets import Treeset 
# from stack import LinkedStack
# from hashtable import HashTable
# from linkedlist import LinkedList

# # hashtable = {}

# def open_file(length):
#     ''' Return words that are length of input word''' 
#     # get words from the words file
#     file = open("/usr/share/dict/words", "r")
#     words_list = file.read().split("\n")
#     file.close()

#     # Returns set of words in length 
#     return Treeset([word for word in words_list if len(word) == length])

# def reconfigure(word):
#     '''Returns the items in common in a string from the two sets '''
#     anagrams = list(permutations(word))
#     # convert this to a list of str, not tuple
#     anagrams = [''.join(list(word)) for word in anagrams]
#     # convert this to a Set
#     anagrams = Treeset(anagrams)
#     # generate the set of all English words in the dictionary file
#     actual_words = open_file(len(word))
#     # find the intersection between the two
#     overlap = anagrams.intersection(actual_words)
#     # dump all the words into a LinkedList, and return the head
#     unscrambled_words = LinkedList(word for word in overlap.collection.keys())
#     if unscrambled_words.head is not None:
#         return unscrambled_words.head.data
#     else:
#         return 'Word Does not exist'


# def solve_puzzle(jumbled_list):
#     '''solves jumble by unscrambling a list of words '''
#     # create a dictionary to store the words
#     hashtable = HashTable(len(jumbled_list))
    
#     jumbled_list = [reconfigure(word) for word in jumbled_list]

#     for i in range(len(jumbled_list)):
#         print(f"'{jumbled_list[i]}'--> '{jumbled_list[i]}'" )
#         # store indices we're interested in at each solved word
#     letters_of_interest = [
#         jumbled_list[0][2] + jumbled_list[0][4],
#         (jumbled_list[1][0] + jumbled_list[1][1] +
#          jumbled_list[1][3]),
#         jumbled_list[2][4],
#         jumbled_list[3][3] + jumbled_list[3][4],
#     ]

#     solution = ''
#     for letter in letters_of_interest:
#         solution += letter
#     return solution
 


# if __name__ == '__main__':
#     first_four = HashTable(4)
#     jumbled = ['tefon','sokik','niumem','siconu']
#     print(f'The answer to the jumble is: {solve_puzzle(jumbled)}')


'''2nd Implementation with a binary search tree''' 
# from binarytree import BinarySearchTree, BinaryTreeNode


# String we want to unscramble
scrambled = ['lbal']

# Helper functions to FILTER DOWN DICTIONARY WORDS
# Search for all words in python dictionary that have the same length of letters as the scrambled string
def filter_dict_string_length(scrambled_string):
    for index in python_dictionary():
        for i in scrambled_string:
            if len(index) == len(i):
                print(index)
# find words that include share double letters, if scrambled word includes double letters
# def matching_chars(scrambled_string)

# Grabs all words from BUILT IN PYTHON DICTIONARY
def get_file_lines(filename):
    '''OPEN the FILE _WITHIN_ a function, you DON'T HAVE TO TYPE file.close()!!!!!'''
    with open(filename, "r") as f:
        lines = f.readlines() 
        strip_line = [word.strip() for word in lines]
    return strip_line

def python_dictionary():
    lines = get_file_lines("/usr/share/dict/words")
    # print(lines)
    return lines

if __name__ == '__main__':
    python_dictionary()
