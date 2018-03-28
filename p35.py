__author__ = "Janna Timmer"

from math import *

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

def generate_primes(max):
	primes = []
	for num in range(2, max):#(1, 100000):
		if is_prime(num):
			primes.append(num)
	return primes

primes = generate_primes(1000000)

circle_primes = []
total = 0

for prime in primes:
	circles = 0
	prime_str = str(prime)
	for num in range(len(prime_str)):
		if prime_str > 1:
			prime_str = prime_str[1:] + prime_str[0]
			# print str(prime) + " / " + prime_str
		if is_prime(int(prime_str)):
			circles += 1
	if circles == len(prime_str) and prime_str not in circle_primes:
		total += 1
		circle_primes.append(prime)
		
		
print total - 1