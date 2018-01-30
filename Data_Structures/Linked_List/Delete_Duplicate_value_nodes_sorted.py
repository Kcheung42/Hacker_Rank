# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Delete_Duplicate_value_nodes_sorted.py             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/25 14:44:14 by kcheung           #+#    #+#              #
#    Updated: 2018/01/25 15:09:29 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You're given the pointer to the head node of a sorted linked list, where the data
in the nodes is in ascending order. Delete as few nodes as possible so that the
list does not contain any value more than once. The given head pointer may be
null indicating that the list is empty.

For now do not be concerned with the memory deallocation. In common abstract data
structure scenarios, deleting an element might also require deallocating the
memory occupied by it. For an initial intro to the topic of dynamic memory
please consult: http://www.cplusplus.com/doc/tutorial/dynamic/

Input Format 
You have to complete the Node* RemoveDuplicates(Node* head) method which takes
one argument - the head of the sorted linked list. You should NOT read any
input from stdin/console.

Output Format 
Delete as few nodes as possible to ensure that no two nodes have the same data.
Adjust the next pointers to ensure that the remaining nodes form a single sorted
linked list. Then return the head of the sorted updated linked list.
Do NOT print anything to stdout/console.

Sample Input

1 -> 1 -> 3 -> 3 -> 5 -> 6 -> NULL
NULL
Sample Output

1 -> 3 -> 5 -> 6 -> NULL
NULL
'''

"""
Delete duplicate nodes
head could be None as well for empty list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
self.data = data
self.next = next_node

return back the head of the linked list in the below method.
"""

class Node:

	def __init__(self, data, next_node=None):
		self.data = data
		self.next = next_node

def RemoveDuplicates(head):
	if head is None:
		return
	cur = head
	prev = head
	while cur is not None:
		cur = prev.next
		if cur is None:
			return
		if cur.data == prev.data:
			prev.next = cur.next
		else:
			prev = cur
	return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)

RemoveDuplicates(head)
temp = head
while(temp):
	print(temp.data)
	temp = temp.next
