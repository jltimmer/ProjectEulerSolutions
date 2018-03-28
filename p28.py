__author__ = "Janna Timmer"

def on_diagonal(row, col, last_row, last_col):
	if row == col:
		return True
	if row != last_row / 2 and row + col == last_row:
		return True
	return False

rows = []

spiral_size = 1001
for row in range(spiral_size):
	this_row = []
	for col in range(spiral_size):
		this_row.append(0)
		
	rows.append(this_row)
	
middle = spiral_size / 2

row_add = middle
min_rows = middle 	 	#1
max_rows = middle + 1	#3
rows_added = 0

col_add = middle
min_cols = middle		#2
max_cols = middle + 1	#3
activity = "columnup"

for add_num in range(1, 1002002):
	# print row_add, col_add
	rows[row_add][col_add] = add_num
	
	if activity == "columnup":
		if col_add < max_cols:
			col_add += 1
		if col_add == max_cols:
			activity = "rowup"
			min_cols -= 1
	
	elif activity == "rowup":
		if row_add < max_rows:
			row_add += 1
		if row_add == max_rows:
			activity = "columndown"
			min_rows -= 1
			
	elif activity == "columndown":
		if col_add > min_cols:
			col_add -= 1
		if col_add == min_cols:
			activity = "rowdown"
			max_cols += 1
	
	elif activity == "rowdown":
		if row_add > min_rows:
			row_add -= 1
		if row_add == min_rows:
			activity = "columnup"
			max_rows += 1
			

sum = 0
for row in range(len(rows)):
	for col in range(len(rows[row])):
		if on_diagonal(row, col, len(rows) - 1, len(rows) - 1):
			sum += rows[row][col]

print sum