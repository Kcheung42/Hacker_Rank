# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01b.Preorder_Traversal.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/14 17:37:19 by kcheung           #+#    #+#              #
#    Updated: 2018/02/26 14:00:45 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
PreOrder Tree traversal Without Recursion
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def preOrder(root):
	if root is None:
		return
	stack = []
	stack.append(root)
	while(len(stack) > 0):
		node = stack.pop()
		print(node.data, end=' ')
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

preOrder(root)
print('\n', end='')
