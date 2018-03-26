# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Scratch.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/28 19:10:22 by kcheung           #+#    #+#              #
#    Updated: 2018/02/03 14:23:21 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a Scratch pad for Python Practice coding

class MinHeap():
	def __init__(self):
		self.heap = []
		self.currentSize = 0

	def heapifyUp(self, i):
		parent = (i-1) // 2
		while parent >= 0:
			if self.heap[i][1] < self.heap[parent][1]:
				# print("swapping Parent:{} with {}".format(self.heap[parent][1], self.heap[i][1]))
				self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
			# print("parent:{}".format(parent))
			i = parent
			parent = (parent - 1) // 2
			# print("next parent:{}".format(parent))

	def heapPush(self, value):
		self.heap.append(value)
		# print("appending:{}".format(value))
		# print(self.heap)
		self.currentSize += 1
		self.heapifyUp(self.currentSize - 1)
		pass

	def getSmallerChild(self, i):
		if 2 * i + 2 > self.currentSize - 1:
			return 2 * i + 1
		else:
			if self.heap[2 * i + 1] < self.heap[2 * i + 2]:
				return 2 * i + 1
			else:
				return 2 * i + 2

	def heapifyDown(self, i):
		while 2 * i + 1 <= self.currentSize - 1:
			smaller = self.getSmallerChild(i)
			if self.heap[smaller][1] < self.heap[i][1]:
				self.heap[smaller], self.heap[i] = self.heap[i], self.heap[smaller]
			i = smaller

	def heapPop(self):
		pop = self.heap[0]
		# print("popping:{}".format(pop))
		self.heap[0] , self.heap[self.currentSize - 1] = self.heap[self.currentSize - 1], self.heap[0]
		self.heap.pop()
		self.currentSize -= 1
		self.heapifyDown(0)
		return pop



class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		k = len(primes)
		h = MinHeap()
		uglies = [0] * n
		for i,val in enumerate(primes):
			h.heapPush((i, val))
		print(h.heap)
		i = 0
		while( i < n ):
			k, uglies[i] = h.heapPop()
			h.heapPush(k, uglies[i] * primes[k])
			print(uglies[i])
			i += 1
		return uglies[-1]

s = Solution()
primes = [2,7,13,19]
n = 12
s.nthSuperUglyNumber(12, primes)
# def heapsort(iterable):
# 	h = []
# 	for value in iterable:
# 		heappush(h, value)
# 	return [heappop(h) for i in range(len(h))]
