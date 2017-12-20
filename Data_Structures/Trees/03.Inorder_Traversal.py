# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.Inorder_Traversal.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/28 20:51:08 by kcheung           #+#    #+#              #
#    Updated: 2017/11/28 20:53:06 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def inOrder(root):
	if root is None:
		return
	inOrder(root.left)
	print(root.data),
	inOrder(root.right)
