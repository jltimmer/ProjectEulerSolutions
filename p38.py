__author__ = "Janna Timmer"

from itertools import *

prm = permutations('123456789')
pandas = []

for pan in prm:
	pan_int = int(pan[0] + pan[1] + pan[2] + pan[3] + pan[4] + pan[5] + pan[6] + pan[7] + pan[8])
	if pan_int > 99999999:
		pandas.append(pan_int)
		
# print pandas

for n in range(1, 10000):
	result = ""
	for k in range(1, n + 1):
		result += str(n * k)
		if result[0] != '9' or len(result) > 9:
			break
		if int(result) in pandas:
			print result