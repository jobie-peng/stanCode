"""
File: boggle.py
Name: Monica Peng
----------------------------------------
This function finds all the words given by a SIZE * SIZE board of characters input by user.
This file put the dictionary in a list of 26 subsets (from a to z) and includes the prefix check function.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4		# Defines the size of the board which is always a square


def main():
	"""
	This function finds all the words given by a SIZE * SIZE board of characters input by user.
	"""
	start = time.time()

	print(f'Boggle Solver! Please input {SIZE} characters with one space in between in each of the {SIZE} rows.')

	boggle = []						# Store the list of characters user input
	found_words = []				# Store the list of words found in dictionary
	words_list = read_dictionary()	# Initialise the dictionary list

	for i in range(SIZE):
		word_row = input(f'{i+1} row of letters: ')
		if not check_if_legal(word_row):
			return print('Illegal input')
		boggle.append(word_row.lower().split())

	for i in range(SIZE):
		for j in range(SIZE):
			search_word(boggle, words_list, i, j, '', found_words)

	print(f'There are {len(found_words)} words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_word(boggle, words_list, i, j, current_s, found_words):
	"""
	:param boggle: list, list of characters input by user
	:param words_list: list, list of all the words in dictionary
	:param i: int, the row of the boggle board
	:param j: int, the col of the boggle board
	:param current_s: str, the current string by putting together the character
	:param found_words: list, list of all the words found in dictionary
	"""
	# If it goes outside the board or the character has been used before, exit the function
	if i < 0 or i >= SIZE or j < 0 or j >= SIZE or boggle[i][j] == '*':
		return

	# If the current string >= 2 characters, and it doesn't start with the prefix in dictionary, exit the function
	if len(current_s) >= 2 and not has_prefix(current_s, words_list):
		return

	# Choose
	current_s += boggle[i][j]
	if len(current_s) >= 4 and current_s in words_list[ord(current_s[0])-97] and current_s not in found_words:
		found_words.append(current_s)
		print(f'Found \"{current_s}\"')

	original_ch = boggle[i][j]
	boggle[i][j] = '*'	# Mark the cell as visited

	# Explore
	# Adjacent cells
	search_word(boggle, words_list, i - 1, j, current_s, found_words)		# Up
	search_word(boggle, words_list, i + 1, j, current_s, found_words)		# Down
	search_word(boggle, words_list, i, j - 1, current_s, found_words)		# Left
	search_word(boggle, words_list, i, j + 1, current_s, found_words)		# Right
	# Diagonal cells
	search_word(boggle, words_list, i - 1, j - 1, current_s, found_words)	# Up-Left
	search_word(boggle, words_list, i - 1, j + 1, current_s, found_words)	# Up-Right
	search_word(boggle, words_list, i + 1, j - 1, current_s, found_words)	# Down-Left
	search_word(boggle, words_list, i + 1, j + 1, current_s, found_words)	# Down-Right

	# Un-choose
	boggle[i][j] = original_ch


def check_if_legal(word_row: str) -> bool:
	if len(word_row) != SIZE*2-1:		# Check if the length is correct
		return False
	else:
		for i in range(len(word_row)):	# Check if the format is legal, (SIZE) letters with (SIZE-1) spaces
			if i % 2 == 0 and not word_row[i].isalpha():
				return False
			elif i % 2 == 1 and word_row[i] != ' ':
				return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each subset starting with each character.
	"""
	words_list = []
	for i in range(26):
		subset = []
		with open(FILE, 'r') as f:
			for line in f:
				if ord(line.strip()[0]) == i + 97:
					subset.append(line.strip())
		words_list.append(subset)

	return words_list


def has_prefix(sub_s, words_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param words_list: list, a dictionary which contains all the words that we search the sub_s in.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in words_list[ord(sub_s[0])-97]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
