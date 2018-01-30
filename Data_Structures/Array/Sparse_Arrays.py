# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Sparse_Arrays.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/25 14:39:17 by kcheung           #+#    #+#              #
#    Updated: 2018/01/25 14:41:28 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/bin/python3

import sys

def sparse_arrays(n, arr, q, queries):
	for q in queries:
		count = 0
		for a in arr:
			if q == a:
				count +=1
		print(count)

if __name__ == "__main__":
	n = int(input())
	arr = []
	for i in range(n):
		el = input()
		arr.append(el)
	q = int(input())
	queries = []
	for i in range(q):
		el = input()
		queries.append(el)
	sparse_arrays(n, arr, q, queries)
    # print (" ".join(map(str, result)))
