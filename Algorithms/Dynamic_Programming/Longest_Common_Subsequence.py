# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Longest_Common_Subsequence.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/21 13:17:26 by kcheung           #+#    #+#              #
#    Updated: 2017/12/21 15:18:05 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##hint Make a matrix see notes

def printLCS(L,m,n,X):
	result = []
	while L[m][n] != 0:
		if L[m-1][n] != L[m][n] and L[m][n-1] != L[m][n]: #if
			result.insert(0,X[m-1])
			m -=1
			n -=1
		elif L[m-1][n] == L[m][n]:
			m -= 1
		elif L[m][n-1] == L[m][n]:
			n -= 1
		L[m][n] = L[m][n]
	return(result)

def LCS(X, Y):
	m = len(X)
	n = len(Y)
	L = [[0] * (n+1) for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	result = printLCS(L, m, n, X)
	for i in range(len(result)):
		print(result[i], end=' ')
	print()
	return(L[m][n])

m, n  = map(int, input().split())
X = list(map(int, input().strip().split(' ')))
Y = list(map(int, input().strip().split(' ')))

LCS(X,Y)
