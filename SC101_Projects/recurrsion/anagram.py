"""
File: anagram.py
Name: Monica Peng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    This program finds all the anagram(s) through recursion using a word user provided.
    It then returns all the word(s) when they are found in the dictionary,
    prints a list of anagrams at the end. It stops when user input the EXIT constant.
    """
    start = time.time()

    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    # Create a dictionary of all the words in the dictionary
    words_list = read_dictionary()

    while True:
        word = input('Find anagrams for: ')
        if word == str(EXIT):
            break
        else:
            anagram_list = []
            anagram_list = find_anagrams(word, words_list, anagram_list)
            # Print all the anagrams found
            print(f'{len(anagram_list)} anagrams: {anagram_list}')

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads the dictionary.txt and return them in a dictionary.
    """
        words_list = {}
        with open(FILE, 'r') as f:
            for line in f:
                words_list[line.strip()] = 'none'
        return words_list


def find_anagrams(s, words_list, anagram_list, current_s='', search=True):
    """
    :param s: str, a word given by the user.
    :param words_list: list, a dictionary which contains all the words.
    :param anagram_list: list, a list of all the anagram found.
    :param current_s: str, current anagram.
    :param search: boolean, controls the first print of searching.
    :return: list, anagrams exist in dictionary and not doubling up.
    """
    # Print searching at the start
    if search:
        print('Searching...')

    if len(s) == 0:
        # Base case
        # Print only if the anagram is in the dictionary or not already in the list
        if current_s in words_list and current_s not in anagram_list:
            print(f'Found: {current_s}')
            anagram_list.append(current_s)
            # Print searching after each anagram is found
            print('Searching...')
    else:
        for i in range(len(s)):
            # Choose
            remaining_s = s[:i] + s[i + 1:]
            # Explore and Un-choose
            find_anagrams(remaining_s, words_list, anagram_list, current_s + s[i], False)

    return anagram_list


def has_prefix(sub_s, words_list):
    """
    :param sub_s: str, a substring of a string.
    :param words_list: list, a dictionary which contains all the words that we search the sub_s in.
    :return: boolean, if sub_s is found in words_dic, return TRUE, otherwise FALSE.
    """
    for word in words_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
