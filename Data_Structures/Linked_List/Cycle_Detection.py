# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Cycle_Detection.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/25 15:14:58 by kcheung           #+#    #+#              #
#    Updated: 2018/01/25 15:21:46 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
	runner = head
	current = head
	while(current is not None):
		runner = runner.next
		if runner is None:
			return False
		elif runner == current:
			return True
		runner = runner.next
		current = current.next
		if current == runner:
			return True
