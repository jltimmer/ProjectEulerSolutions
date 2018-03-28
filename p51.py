__author__ = "Janna Timmer"

from itertools import permutations
from math import sqrt

# Partial code from is_prime may have been borrowed
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def unique(iterable):
	seen = set()
	for x in iterable:
		if x in seen:
			continue
		seen.add(x)
		yield x

def create_locations(length, num_changed):
	#create permutations for locations
		
		locations = ""
		for spot in range(length): #create location template to permutate
			if (spot < length - num_changed):
				locations += "o"
			else:
				locations += "x"
		
		perms = permutations(locations)
		for uniq in unique(perms):
			perm_str = ""
			for digit in uniq:
				perm_str += digit
				
			needed_perms.append(perm_str)
			
		return needed_perms

		
locs = []
for length in range(9):
	needed_perms = []
	for num_changed in range(1, length):
		create_locations(length, num_changed)
	locs.append(needed_perms)

for num in range(120000, 150000):
	for loc in locs[len(str(num))]: #for each template
		family = []
		count = 0
		for new_digit in range(10): #0-9 replace digit
			if len(family) + 10 - new_digit < 8:
				break
			test_num = str(num)
			
			for i in range(len(loc)): #for each letter in this template
				if loc[i] == 'x': #if letter is an x
					test_num = test_num[0:i] + str(new_digit) + test_num[i+1:]
			if test_num[0] == '0':
				continue
			if is_prime(int(test_num)):
				count += 1
				# print loc, new_digit, test_num
				family.append(test_num)
		if count >= 8:
			print family