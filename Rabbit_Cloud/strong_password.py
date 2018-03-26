#!/bin/python3

import sys

def isSet(flags, n):
	if flags&2**n == 2**n:
		return True
	return False

def setFlag(flags, n):
	return flags | 2**n

def minimumNumber(n, password):
# Return the minimum number of characters to make the password strong
	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"
	flags = 0
	for p in password:
		if not isSet(flags, 0)  and p in numbers:
			flags = setFlag(flags, 0)
		if not isSet(flags, 1)  and p in lower_case:
			flags = setFlag(flags, 1)
		if not isSet(flags, 2)  and p in upper_case:
			flags = setFlag(flags, 2)
		if not isSet(flags, 3)  and p in special_characters:
			flags = setFlag(flags, 3)
	fail = 4
	while flags > 0:
		if flags % 2 == 1:
			fail -= 1
		flags = flags >> 1
		# flags //= 2
	diff = 6 - n
	return max(fail, diff)

if __name__ == "__main__":
	n = int(input().strip())
	password = input().strip()
	answer = minimumNumber(n, password)
	print(answer)
