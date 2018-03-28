__author__ = "Janna Timmer"

def find_palindrome(num):
	num_str = str(num)
	reverse = ""
	for digit in range(len(num_str) - 1, -1, -1):
		reverse = reverse + num_str[digit]
	return int(reverse)

def is_palindrome(num):
	num_str = str(num)
	reverse = ""
	for digit in range(len(num_str) - 1, -1, -1):
		reverse = reverse + num_str[digit]
	return num == int(reverse)

def lychrel():
	total = 0
	lych = 0
	for num in range(10000):
		lych += 1
		tries = 0
		sum = num
		while tries < 50:
			if is_palindrome(sum + find_palindrome(sum)):
				lych -= 1
				break
			else:
				tries += 1
				sum = sum + find_palindrome(sum)
	return lych
				
print lychrel()