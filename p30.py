__author__ = "Janna Timmer"

powers_sums = []

for num in range(2, 1000000):
	sum = 0
	num_str = str(num)
	for digit in num_str:
		sum += int(digit)**5
	if sum == num:
		powers_sums.append(num)
		
num_sum = 0
for number in powers_sums:
	num_sum += number
	
print powers_sums
print num_sum