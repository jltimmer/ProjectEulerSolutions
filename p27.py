__author__ = "Janna Timmer"

from math import sqrt

n = 0
count = 0
ab = [0, 0]
max = 0

# Partial code from is_prime may or may not have been borrowed; I can't remember
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

for a in range(-999, 1000):
	for b in range(-999, 1000):
		count = 0
		n = 0
		while (n**2 + a*n + b) > 0 and is_prime(n**2 + a*n + b):
			count += 1
			n += 1
		if count > max:
			max = count
			ab[0] = a
			ab[1] = b
			
print ab
print max
print ab[0] * ab[1]