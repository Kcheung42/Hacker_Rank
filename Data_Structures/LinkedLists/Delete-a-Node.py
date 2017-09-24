#!/usr/local/bin/python3
"""
Delete a Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
	if head is None:
		return head
	if position == 0:
		head = head.next
	else:
		cur = head
		for i in range(position - 1):
			cur = cur.next
			if cur is None:
				break
		if cur is None:
			return head
		cur.next = cur.next.next
	return head
