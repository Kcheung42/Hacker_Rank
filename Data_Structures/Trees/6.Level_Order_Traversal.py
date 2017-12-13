"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def levelOrder(root):
	#Write code Here
	if root is None:
		return

	q = []

	q.append(root)
	while len(q) > 0:
		pop = q.pop(0)
		print(pop.data),
		if pop.left is not None:
			q.append(pop.left)
		if pop.right is not None:
			q.append(pop.right)
