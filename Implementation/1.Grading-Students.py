#!/bin/python3

import sys

def next_five(g):
	if g % 5 > 0:
		return g + 5 - (g % 5)
	return g

def solve(grades):
	# Complete this function
	results = []
	for g in grades:
		if g >= 38:
			dif = next_five(g) - g
			if dif < 3:
				results.append(next_five(g))
			else:
				results.append(g)
		else:
			results.append(g)
	return results

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
	grades_t = int(input().strip())
	grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
