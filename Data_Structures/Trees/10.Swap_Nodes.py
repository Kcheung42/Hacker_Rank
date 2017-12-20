#!/bin/python3
class Node:

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.depth = 1

	def swapOperation(self):
		self.left = temp
		self.left = self.right
		self.right = temp

# def printInorder(root):
# 	if root is None:
# 		return
# 	printInorder(root.left)
# 	print(root.data, end=' '),
# 	printInorder(root.right)

# def swap(root, target,  depth):
# 	if root is None:
# 		return
# 	swap(root.left, target, depth+1)
# 	swap(root.right,target, depth+1)
# 	if depth % target == 0:
# 		root.left , root.right = root.right , root.left

def printInorder(root):
	current = root 
	s = []
	done = 0
	while(True):
		if current is not None:
			s.append(current)
			current = current.left 
		else:
			if(len(s) >0 ):
				current = s.pop()
				print(current.data, end=' '),
				current = current.right 
			else:
				break

def swap(root, target,  depth):
	q = []
	q.append((root, 1))
	while q != []:
		node,depth = q.pop(-1)
		if node.left:
			q.append((node.left, depth + 1))
		if node.right:
			q.append((node.right, depth + 1))
		if depth % target == 0:
			node.left , node.right = node.right, node.left

def main():
	n = int(input())
	root = Node(1)
	q = []
	q.append(root)
	for i in range(n):
		line = list(map(int, input().strip().split(' ')))
		if line[0] != -1 :
			node = Node(line[0])
			q.append(node)
			q[i].left = node
		if line[1] != -1 :
			node = Node(line[1])
			q.append(node)
			q[i].right = node

	swaps = int(input())
	toSwap = []
	for i in range(swaps):
		toSwap.append(int(input()))
	
	for i in range(swaps):
		swap(root, toSwap[i], 1)
		printInorder(root)
		print('\n', end='')

if __name__ == '__main__':
	main()
