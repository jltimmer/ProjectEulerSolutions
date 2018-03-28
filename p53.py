__author__ = "Janna Timmer"

def p53():
	count = 0
	for n in range(23, 101):
		for r in range(1, n + 1):
			size = combination(n, r)
			if size > 1000000:
				count += 1
	return count
	
def combination(n, r):
	n_fact = n
	r_fact = r
	n_r_fact = n - r
	
	for num in range(1, n):
		n_fact *= num
	for num2 in range(1, r):
		r_fact *= num2
	for num3 in range(1, n-r):
		n_r_fact *= num3
		
	if r_fact * n_r_fact > 0:
		return n_fact / (r_fact * n_r_fact)
	
print p53()