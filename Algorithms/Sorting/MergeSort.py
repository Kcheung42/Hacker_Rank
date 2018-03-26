# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MergeSort.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/23 18:26:49 by kcheung           #+#    #+#              #
#    Updated: 2018/03/26 16:56:06 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
# T:O(nlogn) S:O(n)

def merge(arr, left, mid, right):
	nLeft = mid - left + 1
	nRight = right - mid
	L = [0] * nLeft
	R = [0] * nRight
	L[:] = ar[left : mid+1]
	R[:] = ar[mid+1 : right+1]
	i, j, k = 0, 0, left
	while i < nLeft and j < nRight:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	if i < nLeft:
		arr[k:right+1] = L[i:]
	if j < nRight:
		arr[k:right+1] = R[j:]

def mergeSortHelper(arr, start, end):
	if start < end:
		mid = (start + end) // 2
		mergeSortHelper(arr, start, mid)
		mergeSortHelper(arr, mid+1, end)
		merge(arr, start, mid, end)

def mergeSort(arr):
	n = len(arr)
	mergeSortHelper(arr, 0, n-1)

# m = input()
# ar = [int(i) for i in input().strip().split()]
ar = [0,9,8,7,6,5,4,3,2,1]
m = len(ar)
mergeSort(ar)
print(ar)
