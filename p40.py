__author__ = "Janna Timmer"

st = ""

for num in range(1, 1000000):
	st += str(num)
	
print int(st[1000000-1]) * int(st[100000-1]) * int(st[10000-1]) * \
	int(st[1000-1]) * int(st[100-1]) * int(st[10-1]) * int(st[0])