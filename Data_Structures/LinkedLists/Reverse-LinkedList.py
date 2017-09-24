"""
Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 return back the head of the linked list in the below method.
"""

def ReverseUtil(head, cur, prev):
	if (cur.next is None):
		head = cur
		head.next = prev
		return head
	next = cur.next
	cur.next = prev
	Return(ReverseUtil(head, next, cur))


def Reverse(head):
	if head is None:
		return head
	return(ReverseUtil(head, cur, prev))
