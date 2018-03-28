__author__ = "Janna Timmer"

from itertools import *

cubes = []
checked = []

#tests if 2 numbers are permutations of each other
def is_perm_of(a, b):
	try:
		for digit in b:
			if a.count(digit) != b.count(digit):
				return False
		return True
	except: 
		return "Invalid Entry"
	

for num in range(5000, 10000):
	cubed = num**3
	cubes.append(cubed)

test = cubes[0]
for cube_ai in range(len(cubes) - 1):
	count = 0
	for cube_bi in range(cube_ai, len(cubes)):
		if is_perm_of(str(cubes[cube_ai]), str(cubes[cube_bi])) and len(str(cubes[cube_ai])) == len(str(cubes[cube_bi])):
			count += 1
	if count >= 5:
		print cubes[cube_ai]