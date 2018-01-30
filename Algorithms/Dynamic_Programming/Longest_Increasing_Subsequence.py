# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Longest_Increasing_Subsequence.py                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/21 15:23:40 by kcheung           #+#    #+#              #
#    Updated: 2017/12/21 15:33:22 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def LIS(arr):
	n = len(arr)
	lis = [1] * n
	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j]:
				lis[i] = lis[j] + 1
	maximum = max(lis)
	return maximum

n = int(input())
arr = []
for i in range(n):
	list.append(int(input()))

print(LIS(arr))
