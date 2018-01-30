#!/usr/local/bin/python3

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
	new_node = Node(data)
	if head is None:
		return head
	if (position == 0):
		new_node.next = head
		head = new_node
	else:
		cur = head
		for i in range(position-1):
			cur = cur.next
			if(cur is None):
				break;
		new_node.next = cur.next
		cur.next = new_node
	return head

