"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def find_path(root, path, key):
	if root is None:
		return False
	path.append(root)
	if root.data == key:
		return True
	if ((root.left != None and find_path(root.left, path, key)) or (root.right != None and find_path(root.right, path, key))):
		return True
	path.pop()
	return False

def lca(root , v1 , v2):
	if root is None:
		return None
	stackA = [];
	stackB = [];
	if (not find_path(root, stackA, v1) or not find_path(root, stackB, v2)):
		return None
	i = 0
	while (i < len(stackA) and i < len(stackB)):
		if stackA[i] != stackB[i]:
			break
		i += 1
	return stackA[i-1]

  #Enter your code here
