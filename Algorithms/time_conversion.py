#!/bin/python3

import sys

def timeConversion(s):
	# Complete this function
	if s == '12:00:00PM':
		return '12:00:00'
	if s == '12:00:00AM':
		return '00:00:00'
	output = []
	hours = int(s[0:2])
	min = int(s[3:5])
	seconds = int(s[6:8])
	if s[8] == 'P':
		hours = 24 - (12 - hours%12)
	elif s[8] == 'A':
		hours %= 12
	hours = '%02d' %hours
	min = '%02d' %min
	seconds = '%02d' %seconds
	output.append(hours)
	output.append(':')
	output.append(min)
	output.append(':')
	output.append(seconds)
	result = ''.join(output)

	return result

s = input().strip()
result = timeConversion(s)
print(result)

