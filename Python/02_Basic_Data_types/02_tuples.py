# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_tuples.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/03 13:10:03 by kcheung           #+#    #+#              #
#    Updated: 2017/12/03 13:28:49 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Task Given an integer, n and n spaced-sperated integers as input, create a
# tuple, t, of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':
	tup = ();
	n = int(input())
	integer_list = map(int, input().split())
	tup = tuple(integer_list)
	print(hash(tup))
