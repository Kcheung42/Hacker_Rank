# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    06_Write_a_function.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/03 12:13:29 by kcheung           #+#    #+#              #
#    Updated: 2017/12/03 12:22:55 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_leap(year):
	leap = False
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				leap = True
			else:
				leap = False
		else:
			leap = True
	else:
		leap = False
	return leap
