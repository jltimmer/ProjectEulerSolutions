__author__ = "Janna Timmer"

from math import sqrt

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

def trunc():
	sum = 0
	for num in range (23, 1000000):
		if is_prime(num):
			left = num
			right = num
			while len(str(left)) > 1 and len(str(right)) > 1:
				left = str(left)[1:]
				if not is_prime(int(left)):
					break
					
				right = right / 10
				if not is_prime(right):
					break
					
				if len(str(left)) == 1 and len(str(right)) == 1:
					sum += num
	return sum		
					
print trunc()