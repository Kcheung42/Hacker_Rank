# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Merge_Sort.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/23 18:26:49 by kcheung           #+#    #+#              #
#    Updated: 2018/01/23 18:49:29 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
# T:O(nlogn) S:O(n)

def merge(arr, l, m, r):
	nl = m - l + 1
	nr = r - m
	L = [0] * nl
	R = [0] * nr
	for i in range(nl):
		L[i] = arr[i + l]
	for i in range(nr):
		R[i] = arr[i + m + 1]

	i, j, k = 0, 0, l
	while i < nl and j < nr:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < nl:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < nr:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSortHelper(arr, start, end):
	if start < end:
		m = (start + end) // 2
		mergeSortHelper(arr, start, m)
		mergeSortHelper(arr, m + 1, end)
		merge(arr, start, m, end)

def mergeSort(arr):
	n = len(ar)
	mergeSortHelper(arr, 0, n-1)

# m = input()
# ar = [int(i) for i in input().strip().split()]

ar = [0,9,8,7,6,5,4,3,2,1]
m = len(ar)
mergeSort(ar)
print(ar)
