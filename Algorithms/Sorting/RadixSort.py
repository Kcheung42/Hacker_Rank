# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    RadixSort.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/31 18:20:01 by kcheung           #+#    #+#              #
#    Updated: 2018/03/01 16:34:18 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# T:O(nk) S:O(n+k)
# Use Radix sort if the range of digits

def countingSort(arr, exp):
	n = len(arr)
	output = [0] * n
	counts = [0] * 10 #array of [0 - 9] number of digits
	for i in range(n):
		index = (arr[i] // exp) % 10
		counts[index] += 1
		print(counts)
	for i in range(1, 10):
		counts[i] += counts[i-1]
	print(counts)
	i = n-1
	while i >= 0:
		# print('output:{}'.format(output))
		index = (arr[i] // exp) % 10
		output[counts[index]-1] = arr[i]
		counts[index] -= 1
		i -= 1
	# print('output:{}'.format(output))
	
	i = 0
	for i in range(0,n):
		arr[i] = output[i]

def radixSort(arr):
	m = max(arr)
	n = len(arr)
	exp = 1
	while m // exp > 0 :
		print("==============================")
		countingSort(arr,exp)
		exp *= 10
	pass

# s = [9,8,7,6,5,4,3,2,1]
s = [2322222222222222222222222222222222222222222222222222222,3,2,44,45,42]
radixSort(s)
print(s)
