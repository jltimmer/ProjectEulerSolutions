__author__ = "Janna Timmer"

from itertools import *

x = permutations('0123456789')

number = 1
while number <= 1000000:
	perm = x.next()
	number += 1
	
print perm