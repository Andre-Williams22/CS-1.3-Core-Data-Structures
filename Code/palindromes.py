#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def cleans_palindrome(text): 
    ''' Function to clean the text before checking to see if it's a palindrome '''
    clean = "?!.,:;-_'"
    for item in clean:
        text = text.replace(item, '') # cleans the text returning only the string
    return text 

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    #return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    #once implemented, change is_palindrome to call is_palindrome_iterative
    #to verify that your iterative implementation passes all tests
    text = cleans_palindrome(text) # calls helper function to clean the text
    left = 0 
    right = len(text) - 1
    if len(text) < 1: # checks length is less than 1 
        return True
    while left <= right: 
        if text[left].lower() != text[right].lower(): # checks to find if the ends of the strings are identical
            return False
        left += 1 # increment the left by 1 
        right -= 1 # increment the right by 1 
    return True

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    if left == None:
        left = 0
        right = len(text) - 1
        best = " ?!,.;:-_'"
        for char in best:
            text = text.replace(char, '')
    if len(text) < 1:
        return True
    if left <= right and right < len(text):
        if text[left].lower() != text[right].lower():
            return False
        return is_palindrome_recursive(text, left+1, right-1)
    #return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
