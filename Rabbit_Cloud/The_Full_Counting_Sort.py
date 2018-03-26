#!/bin/python3

import sys

if __name__ == "__main__":
	n = int(input().strip())
	for a0 in range(n):
		x, s = input().strip().split(' ')
		x, s = [int(x), str(s)]
