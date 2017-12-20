"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return(len(self.items))

def topView(root):
	#Write your code here
	if root is None:
		return
	m = set({})
	topview = []
	q = Queue()
	q.enqueue((root, 0))
	while q.isEmpty() is False:
		node , hd = q.dequeue();
		if hd not in m:
			topview.append((node.data, hd))
			m.add(hd)
		if node.left is not None:
			q.enqueue((node.left, hd - 1))
		if node.right is not None:
			q.enqueue((node.right, hd + 1))
	topview = sorted(topview, key=lambda x: x[1])
	for i in topview:
		print(i[0]),
