# **************************************************************************** #
#                                                                              #
#                                                     .-. .-')                 #
#    2.Apple-and-Orange.py                              :+:      :+:    :+:    #
#                                                     ,--. ,--.   .-----.      #
#    By: kcheung <kcheung@42.fr>                      |  .'   /  '  .--./      #
#                                                     |      /,  |  |('-.      #
#    Created: 2017/10/20 11:59:25 by kcheung          |     ' _)/_) |OO  )     #
#    Updated: 2017/10/20 11:59:26 by kcheung          ###   ########.fr        #
#                                                     |  |\   \(_'  '--'\      #
# **************************************************************************** #

#!/bin/python3

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

count_a = 0
count_b = 0
for ap in apple:
	if a + ap >= s and a + ap <= t:
		count_a += 1
for oj in orange:
	if b + oj >= s and b + oj <= t:
		count_b += 1
print (count_a)
print (count_b)


