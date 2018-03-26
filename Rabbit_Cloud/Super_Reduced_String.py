#!/bin/python3

import sys

def find_pairs(s):
	n = len(s)
	for i in range(n-1):
		if s[i] == s[i+1]:
			return (i, i + 1)
		i += 1
	return (0,0)

def super_reduced_string(s):
	# Complete this function
	str = ''
	ret = []
	n = len(s)
	if s is None:
		return('Empty String')
	if n == 1:
		return s
	while True:
		(a,b) = find_pairs(s)
		if (a,b) == (0,0):
			break
		else:
			s = s[:a] + s[b+1:]
	if len(s) == 0:
		return "Empty String"
	return s

s = input().strip()
result = super_reduced_string(s)
print(result)

