__author__ = "Janna Timmer"

combos = []

for num in range(2, 101):
	for num2 in range(2, 101):
		if num**num2 not in combos:
			combos.append(num ** num2)
			
print len(combos)