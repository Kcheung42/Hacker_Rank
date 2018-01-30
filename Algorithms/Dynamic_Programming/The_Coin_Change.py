# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.The_Coin_Change.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/11 12:09:20 by kcheung           #+#    #+#              #
#    Updated: 2018/01/11 12:09:21 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

import sys

def getWaysHelper(target, c, index, hashMap):
	if (target == 0):
		return (1)
	if(index >= len(c)):
		return (0)
	key = str(n) + '-' + str(index)
	if key in hashMap:
		return hashMap[key]
	coinsValue =  0;
	ways = 0;
	while(coinsValue <= n):
		remaining = target - coinsValue
		ways += getWaysHelper(remaining, c, index + 1, hashMap)
		coinsValue += c[index]
	hashMap[key] = ways
	return ways

def getWays(target, c):
	hashMap = {}
	return (getWaysHelper(target, c, 0, hashMap))

    # Complete this function

# n, m = input().strip().split(' ')
# n, m = [int(n), int(m)]
# c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
n = 100
c = [25, 5, 10, 2]
ways = getWays(n, c)
print (ways)
