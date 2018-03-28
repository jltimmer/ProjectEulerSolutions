__author__ = "Janna Timmer"

from itertools import *

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

# possible = "aa,ab,ac,ad
grid_size = 20
num_pos = grid_size + 1
stops = grid_size * 2 + 1
longest_row_len = grid_size + 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = ''

rows = []
row_len = 1
spaces = grid_size * " "
reached_middle = False
while row_len > 0: #loop to create rows
	this_row = []
	for num in range(row_len):
		this_row.append(0)
	rows.append(this_row)
	
	if row_len == longest_row_len:
		reached_middle = True
		
	if reached_middle:
		row_len -= 1
		spaces += " "
	else:
		row_len += 1
		spaces = spaces[0:-1]
		
total = 1
upper_half = True

rows[0][0] = 1
print rows[0]

for i in range(1, len(rows)):
	
		
	for j in range(len(rows[i])):
		if upper_half:
			if j < len(rows[i]) - 1:
				rows[i][j] = int(rows[i][j]) + int(rows[i-1][j])
			if j > 0:
				rows[i][j] = int(rows[i][j]) + int(rows[i-1][j-1])
				
		else:
			rows[i][j] = int(rows[i][j]) + int(rows[i-1][j])
			rows[i][j] = int(rows[i][j]) + int(rows[i-1][j+1])
				
	if i == grid_size: #when i reaches middle row
		upper_half = False
		
	print rows[i]
	

total = rows[-1][0]
print total