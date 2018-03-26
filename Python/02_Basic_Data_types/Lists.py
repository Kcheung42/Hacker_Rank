# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_Lists.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/03 12:34:05 by kcheung           #+#    #+#              #
#    Updated: 2017/12/03 13:09:50 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	N = int(input())
	l = []
	for i in range(N):
		buffer = input().split(' ')
		command = buffer[0]
		if command == 'insert':
			l.insert(int(buffer[1]), int(buffer[2]))
		elif command == 'print':
			print(l)
		elif command == 'remove':
			l.remove(int(buffer[1]))
		elif command == 'append':
			l.append(int(buffer[1]))
		elif command == 'sort':
			l.sort()
		elif command == 'pop':
			l.pop()
		elif command == 'reverse':
			l.reverse()
		else:
			pass
