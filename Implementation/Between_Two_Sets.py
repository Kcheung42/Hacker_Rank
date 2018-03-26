# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Between_Two_Sets.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/27 21:16:22 by kcheung           #+#    #+#              #
#    Updated: 2017/11/27 22:10:20 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3

import sys

def isfactor_a(x,list):
	for a in list:
		if x % a != 0:
			return False
	return True

def isfactor_b(x,list):
	for b in list:
		if  b % x != 0:
			return False
	return True

def getTotalX(a, b):
	# Complete this function
	count = 0
	for x in range(1,sum(b)):
		if isfactor_b(x,b) and isfactor_a(x,a):
			count += 1
	return count

if __name__ == "__main__":
	n, m = input().strip().split(' ')
	n, m = [int(n), int(m)]
	a = list(map(int, input().strip().split(' ')))
	b = list(map(int, input().strip().split(' ')))
	total = getTotalX(a, b)
	print(total)
