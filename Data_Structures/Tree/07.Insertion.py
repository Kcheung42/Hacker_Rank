"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None
	
	def insert(self, val):
		node = Node(val)
		if self.root is None:
			self.root = node
		if self.root.data > node.data:
			if self.root.left is None:
				self.root.left = node
			else:
				self.root.left = insert(self.root.left, val)
		elif self.root.data < node.data:
			if self.root.right is None:
				self.root.right = node
			else:
				self.root.right = insert(self.root.right, val)

def insertHelper(root, node):
	if root is None:
		root = node
	else:
		if root.data <= node.data:
			if root.right is None:
				root.right = node
			else:
				insertHelper(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insertHelper(root.left, node)

def insert(r,val):
	node = Node(val)
	insertHelper(r, node)
	return r
   #Enter you code here.

# tree = BinarySearchTree()
# tree.insert(4)
# tree.insert(2)
# tree.insert(6)
# tree.insert(1)
# print tree.root.data
# print tree.root.left.data
# print tree.root.right.data
# print tree.root.left.left.data
