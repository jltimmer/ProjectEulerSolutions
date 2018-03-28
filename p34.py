__author__ = "Janna Timmer"

from math import factorial

facts = []
ans_sum = 0

for num in range(3, 100000):
	sum = 0
	num_str = str(num)
	for digit in num_str:
		sum += factorial(int(digit))
	if sum == num:
		facts.append(num)
		
for fact in facts:
	ans_sum += fact
	
print ans_sum