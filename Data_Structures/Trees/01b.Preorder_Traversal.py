
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def preOrder(root):
	if root is None:
		return
	current = root
	stack = []
	stack.append(current)
	while(len(stack) > 0):
		node = stack.pop()
		print(node.data, end=' ')
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

preOrder(root)
print('\n', end='')
