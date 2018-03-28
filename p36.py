__author__ = "Janna Timmer"

palindromes = []

for num in range(1, 1000000):
	num_str = str(num)
	num_reverse = ""
	for i in range(len(num_str) - 1, -1, -1):
		num_reverse = num_reverse + num_str[i]
		
	bin_str = bin(num)[2:]
	bin_reverse = ""
	for i in range(len(bin_str) - 1, -1, -1):
		bin_reverse = bin_reverse + bin_str[i]
		
	if num_str == num_reverse and bin_str == bin_reverse:
		palindromes.append(num)
	
sum = 0
for pal in palindromes:
	sum += pal
print "Sum: " + str(sum)