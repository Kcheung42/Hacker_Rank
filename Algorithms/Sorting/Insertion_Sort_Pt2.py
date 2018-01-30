#!/bin/python
def insertionSort(ar):
	if(len(ar) == 0):
		return
	if(len(ar) == 1):
		print(ar[0])
		return

	for i in range(1,len(ar)):
		cur = ar[i]
		j = i - 1
		while(j >= 0 and cur < ar[j]):
			ar[j+1] = ar[j]
			j -= 1
		ar[j+1] = cur
		print " ".join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
