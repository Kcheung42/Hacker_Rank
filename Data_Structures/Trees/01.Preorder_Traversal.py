# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01.Preorder_Traversal.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/28 20:40:14 by kcheung           #+#    #+#              #
#    Updated: 2017/12/20 11:50:55 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
	if root is None:
		return
	print(root.data),
	preOrder(root.left)
	preOrder(root.right)
