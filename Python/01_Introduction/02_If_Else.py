# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.If_Else.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/03 12:08:58 by kcheung           #+#    #+#              #
#    Updated: 2017/12/03 12:09:01 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	n = int(input())

	if n % 2:
		print('Weird')
	elif (n >= 6 and n <=20):
		print ('Weird')
	else:
		print('Not Weird')
