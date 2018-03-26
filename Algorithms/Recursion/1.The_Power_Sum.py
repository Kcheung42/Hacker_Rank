
def findSum(x, n, arr):
	print(arr)
	if x < 0:
		return 0
	if x == 0:
		return 1
	sum = 0
	for i in range(len(arr)):
		sum += findSum(x-(arr[i]**n), n, arr[arr[i]::])
		if arr[i]**n > x:
			break
	return (sum)

def f(x, n):
	arr = [i for i in range(1,x+1)]
	print(arr)
	return(findSum(x, n, arr))

x = int(input())
n = int(input())
print(f(x,n))
