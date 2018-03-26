#!/bin/python3

import sys

def isMatchingpair(a, b):
	if a =='(' and b == ')':
		return 'YES'
	if a =='{' and b == '}':
		return 'YES'
	if a =='[' and b == ']':
		return 'YES'
	return 'NO'

def isBalanced(s):
	'''
	:type s: str
	:rtype: bool
	'''
	opening = set(['(', '{','['])
	closing = set([')','}',']'])
	stack = []
	for c in s:
		if c in opening:
			stack.append(c)
		elif c in closing:
			if len(stack) > 0:
				pop = stack.pop()
				if isMatchingpair(pop, c) == 'NO':
					return 'NO'
			else:
				return 'NO'
	if len(stack) > 0:
		return 'NO'
	return 'YES'

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		s = input().strip()
		result = isBalanced(s)
		print(result)
