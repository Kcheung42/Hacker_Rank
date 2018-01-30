"""
Find the node at which both lists merge and return the data of that node.
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
self.data = data
self.next = next_node


"""

def len(ll):
	temp = ll
	count = 0
	while(temp):
		count += 1
		temp = temp.next
	return (count)

def FindMergeNode(headA, headB):
	lenA = len(headA)
	lenB = len(headB)

	longer = headA if lenA > headB else headB
	shorter = headB if longer == headA else headA
	dif ==  abs(lenA - lenB)
	for i in range(dif):
		longer = longer.next
	while(longer != shorter):
		longer = longer.next
		shorter = shorter.next

	return(longer)
