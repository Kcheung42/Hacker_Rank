#!/bin/python3

import sys

def leftRotation(a, d):
	# Complete this function
	n = len(a)
	i = d % n
	split = n-i
	a[:] = reversed(a[:])
	a[0:split] = reversed(a[0:split])
	a[split:n] = reversed(a[split:n])
	return(a)

if __name__ == "__main__":
	n, d = input().strip().split(' ')
	n, d = [int(n), int(d)]
	a = list(map(int, input().strip().split(' ')))
	result = leftRotation(a, d)
	print (" ".join(map(str, result)))
