# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.Postorder_Traversal.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/28 20:51:08 by kcheung           #+#    #+#              #
#    Updated: 2017/11/28 20:51:10 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def postOrder(root):
	if root is None:
		return
	postOrder(root.left)
	postOrder(root.right)
	print(root.data),
