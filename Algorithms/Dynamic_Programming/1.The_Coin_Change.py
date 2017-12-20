#!/bin/python3

import sys

def getWaysHelper(n, c, index, hashMap):
	if (n == 0):
		return (1)
	if(index >= len(c)):
		return (0)
	key = str(n) + '-' + str(index)
	if key in hashMap:
		return hashMap[key]
	coinsValue =  0;
	ways = 0;
	while(coinsValue <= n):
		remaining = n - coinsValue
		ways += getWaysHelper(remaining, c, index + 1, hashMap)
		coinsValue += c[index]
	hashMap[key] = ways
	return ways

def getWays(n, c):
	hashMap = {}
	return (getWaysHelper(n, c, 0, hashMap))

    # Complete this function

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print (ways)
