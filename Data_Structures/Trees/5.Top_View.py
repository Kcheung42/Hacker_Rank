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

class Node:
	def __init__(self, data=None):
		self.data =  data
		self.left = None
		self.right = None

def topView(root):
  #Write your code here
  if root is None:
	  return
  m = {}
  q = queue()
  q.enqueue({root.val, 0})

  while q.isEmpty() is False:

	  pass

if __name__ == "__main__":
	topView(root)
