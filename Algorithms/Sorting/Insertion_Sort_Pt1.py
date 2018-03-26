#!/bin/python
def insertionSort(ar):    
	num = ar[-1];
	i = len(ar) - 2;
	while i >= 0 and num < ar[i]:
		ar[i+1] = ar[i]
		i -= 1
		print " ".join(map(str, ar))
	ar[i+1] = num
	print " ".join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
