#!/bin/python3

import sys

def getRecord(s):
	most_count = 0
	least_count = 0
	most_record = s[0]
	least_record = s[0]

	for record in s:
		if record > most_record:
			most_count += 1
			most_record = record
		elif record < least_record:
			least_count += 1
			least_record = record
	return (most_count, least_count)
    # Complete this function
	pass

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
