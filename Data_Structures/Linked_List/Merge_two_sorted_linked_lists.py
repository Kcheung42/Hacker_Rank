"""
Merge two  linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
	if headA is None:
		return headB
	if headB is None:
		return headA
	if headA.data <= headB.data:
		result = headA
		result.next = MergeLists(headA.next, headB)
	else:
		result = headB
		result.next = MergeLists(headA, headB.next)
	return (result)

# def MergeLists(headA, headB):
# 	curA = headA
# 	curB = headB
# 	if curA.data < curB.data:
# 		ret_head = headA
# 	else:
# 		ret_head = headB
# 	while(curA and curB):
# 		if curA.data < curB.data:
# 			nextA = curA.next
# 			curA.next = curB
# 			curA = nextA
# 		else:
# 			nextB = curB.next
# 			curB.next = curA
# 			curB = nextB
# 	return ret_head
