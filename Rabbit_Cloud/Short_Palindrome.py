#!/bin/python3

import sys

def shortPalindrome(s):
	# Complete this function
	n = len(s)
	count = 0
	for i in range(n-3):
		for j in range(i+1, n-2):
			for k in range(j+1, n-1):
				if s[j] == s[k]:
					count += s[k+1:].count(s[i])
	return count % (10**9 + 7)

if __name__ == "__main__":
	# s = input().strip()
	# s = 'abbaab'
	s = 'kkkkkkz'
	result = shortPalindrome(s)
	print(result)
