"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topleft(root):
	if root is None:
		return
	topleft(root.left)
	print(root.data),

def topRight(root):
	if root is None:
		return
	print(root.data),
	topRight(root.right)


def topView(root):
	if root is None:
		return
	topleft(root.left)
	print(root.data),
	topRight(root.right)
