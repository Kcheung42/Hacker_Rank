#!/bin/python3

import sys

def bubSort():
	pass

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

sorted = [int(x) for x in unsorted]
sorted.sort()
for i in range(n):
	print(sorted[i])

# your code goes here
