#!/bin/python3

import sys

def roadsAndLibraries(n, c_lib, c_road, cities):
	# Complete this function

if __name__ == "__main__":
	q = int(input().strip())
	for a0 in range(q):
		n, m, c_lib, c_road = input().strip().split(' ')
		n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
		cities = []
		for cities_i in range(m):
			cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
			cities.append(cities_t)
		result = roadsAndLibraries(n, c_lib, c_road, cities)
		print(result)
