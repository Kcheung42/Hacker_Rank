# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    QHEAP1.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/08 10:05:20 by kcheung           #+#    #+#              #
#    Updated: 2018/03/08 12:08:21 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

from heapq import *

# def heapsearch(h, v):
# 	q = []
# 	q.insert(0,0)
# 	n = len(h)
# 	while(len(q) > 0):
# 		i = q.pop()
# 		if h[i] == v:
# 			return i
# 		left_child = 2*i+1
# 		right_child = 2*i+2
# 		if left_child < n and h[left_child] < v:
# 			q.insert(0,left_child)
# 		if right_child < n and h[right_child] < v:
# 			q.insert(0,right_child)
# 	return -1

def heapsearch(h, v):
	for i in range(len(h)):
		if h[i] == v:
			return i
	return -1

def heapdelete(h, v):
	i = heapsearch(h, v)
	if i >= 0:
		h[i], h[-1] = h[-1], h[i]
		h.pop()
		heapify(h)
	return

def heapq1(commands):
	h = []
	for i in range(len(commands)):
		# print("command:{} on heap:{}".format(commands[i][0], h))
		if commands[i][0] == 1:
			heappush(h, commands[i][1])
		elif commands[i][0] == 2:
			heapdelete(h, commands[i][1])
		elif commands[i][0] == 3:
			if len(h) > 0:
				print(h[0])
			else:
				print([])
		else:
			continue

if __name__ == "__main__":
	n = int(input().strip())
	list = []
	for i in range(n):
		c = input().strip().split(' ')
		if len(c) == 1:
			list.append((int(c[0]),0))
		else:
			list.append((int(c[0]),int(c[1])))
	# list = [(1, 2), (1, 5), (1, 3), (2, 2), (1, 4), (2, 5), (3, 0), (1, 3), (2, 3), (3, 0)]
	# list = [(1,4), (1,9), (3,0),(2,4),(3,0)]
	# list = [(3,0)]
	# print(list)
	heapq1(list)
