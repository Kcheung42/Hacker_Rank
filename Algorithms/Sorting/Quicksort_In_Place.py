# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Quicksort_In_Place.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/12 16:42:01 by kcheung           #+#    #+#              #
#    Updated: 2018/01/23 18:55:57 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
# T:O(n^2) S(log(n))

def partition(arr, start, end):
	pivot = arr[end]
	p_index = start
	for i in range(start, end):
		if arr[i] <= pivot:
			arr[i] , arr[p_index] = arr[p_index] , arr[i]
			p_index += 1
	arr[end], arr[p_index] = arr[p_index], arr[end]
	return p_index

def quickSortHelper(arr, start, end):
	if start < end:
		pi = partition(arr, start, end)
		quickSortHelper(arr, start, pi - 1)
		quickSortHelper(arr, pi + 1,  end)

def quickSort(arr):
	n = len(arr)
	quickSortHelper(arr, 0, n - 1)

s = [9,8,7,6,5,4,3,2,1]
quickSort(s)
print(s)

