# import os
# from itertools import permutations 
# from sets import Treeset 

# hashtable = {}

with open("/usr/share/dict/words", 'r') as fd:
    for line in fd:
        line = line.strip()


# print(hashtable)

# # Function to find permutations of a given string 
# def allPermutations(str): 
#      # Get all permutations of string 'ABC' 
#      permList = permutations(str) 
  
#      # print all permutations 
#      for perm in list(permList): 
#          print (''.join(perm)) 
        
# #print(allPermutations())




# if __name__ == "__main__": 
#     pass

#     # str = 'ABC'
#     # allPermutations(str)

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