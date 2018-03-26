def bubbleSort(ar): #Time:O(n^2) Space:O(1)
	n = len(ar)
	for i in range(n):
		for j in range(n - i - 1):
			if ar[j] > ar[j+1]:
				ar[j],ar[j+1] = ar[j + 1],ar[j]

ar = [9,8,7,6,5,4,3,2,1]
bubbleSort(ar)
print(ar)
