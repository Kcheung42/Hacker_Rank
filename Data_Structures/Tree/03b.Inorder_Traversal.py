
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	if root is None:
		return
	current = root
	s = []
	while(True):
		if current is not None:
			s.append(current)
			current = current.left
		else:
			if len(s) > 0:
				current = s.pop()
				print(current.data, end=' ')
				current = current.right
			else:
				break

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print ("Post Order Traversal of binary tree is")
inOrder(root)
print('\n', end='')
