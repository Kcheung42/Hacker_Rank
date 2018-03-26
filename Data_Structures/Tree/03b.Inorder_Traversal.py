# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03b.Inorder_Traversal.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/26 14:10:14 by kcheung           #+#    #+#              #
#    Updated: 2018/03/19 20:17:54 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	if root is None:
		return
	current = root
	s = []
	while(True):
		if current:
			s.append(current)
			current = current.left
		else:
			if len(s) > 0:
				current = s.pop()
				print(current.data, end=' ')
				current = current.right
			else:
				break

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print ("Post Order Traversal of binary tree is")
inOrder(root)
print('\n', end='')

