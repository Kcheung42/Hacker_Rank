# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Scratch.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/28 19:10:22 by kcheung           #+#    #+#              #
#    Updated: 2017/12/20 11:39:23 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a Scratch pad for Python Practice coding

def PostOrder(root):
	if root is None:
		return
	current = root
	s = []
	while(True):
		while current:
			if current.right is not None:
				s.append(current.right)
			s.append(current)
			current = current.left
		current = stack.pop()
		if current.right is not None and peek(stack) == current.right:
			stack.pop()
			stack.apopend(current)
			current = current.right
		else:
			print(current.data, end=' ')
			current = None
		if len(s) <= 0:
			break
