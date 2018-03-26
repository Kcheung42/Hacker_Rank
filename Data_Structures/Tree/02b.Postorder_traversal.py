# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02b.Postorder_traversal.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/26 14:10:06 by kcheung           #+#    #+#              #
#    Updated: 2018/02/26 14:10:08 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def peek(stack):
	if len(stack) > 0:
		return stack[-1]
	else:
		return None

def postOrder(root):
	if root is None:
		return
	current = root
	stack = []
	while(True):
		while(current):
			if current.right is not None:
				stack.append(current.right)
			stack.append(current)
			current = current.left
		current = stack.pop()
		if current.right is not None and peek(stack) == current.right:
			stack.pop()
			stack.append(current)
			current = current.right
		else:
			print(current.data, end=' ')
			current = None
		if len(stack) <= 0:
			break

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print ("Post Order Traversal of binary tree is")
postOrder(root)
print('\n', end='')
