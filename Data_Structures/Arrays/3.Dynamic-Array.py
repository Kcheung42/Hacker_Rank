#!/usr/local/bin/python3

def main():
	n , q = input().strip().split(' ')
	n , q = int(n), int(q)
	queries = []
	seqList = []
	lastAnswer = 0
	for num in range(n):
		seqList.append(list())
	for query in range(q):
		queries.append(list(map(int, input().strip().split(' '))))
	for q in queries:
		type = q[0]
		x = q[1]
		y = q[2]
		seq = seqList[(x ^ lastAnswer) % n]
		if type == 1:
			seq.append(y)
		elif type == 2:
			lastAnswer = seq[y % len(seq)]
			print(lastAnswer)

if __name__ == "__main__":
	main()
