"""
File: largest_digit.py
Name: Monica Peng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, a number given
	:return: int, returns the largest digit of the number
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, largest_n):
	"""
	:param n: int, a number given
	:param largest_n: int, the current largest digit in each iteration
	:return: int, returns the largest digit of the number
	"""
	if n < 0:
		n = -n

	if n == 0:
		return largest_n
	else:
		if n % 10 > largest_n:
			largest_n = n % 10
		return find_largest_digit_helper(n // 10, largest_n)


if __name__ == '__main__':
	main()
