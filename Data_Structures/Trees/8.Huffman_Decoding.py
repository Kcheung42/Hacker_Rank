"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
	if root is None:
		return
	x = 0
	node = root
	while x < len(s):
		bit = s[x];
		if bit == '1':
			# print("going right:"),
			# print(bit)
			node = node.right
		else:
			# print("going left:"), 
			# print(bit)
			node = node.left
		if node.data != '\0':
			sys.stdout.write(node.data)
			node = root
		x += 1

   #Enter Your Code Here
