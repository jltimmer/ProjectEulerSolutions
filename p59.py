__author__ = "Janna Timmer"

file = open("p059_cipher.txt")
values = file.read().split(",")

letters = "abcdefghijklmnopqrstuvwxyz"
letters2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,1234567890()[]/ '
	
combos = []
for i in range(len(letters)):
	for j in range(len(letters)):
		for k in range(len(letters)):
			
			combos.append([ord(letters[i]), ord(letters[j]), ord(letters[k])])

ciphers = []

for combo in combos:
	wrong_count = 0
	cipher = ""
	english = True
	count = 0
	for value_i in range(len(values)):
		if count > 2:
			count = 0
		cipher += chr(int(values[value_i]) ^ combo[count])
		if cipher[-1] not in letters2:
			wrong_count += 1
		if wrong_count > 5:
			break
		count += 1
		
	if wrong_count > 5:
		continue
	
	if english and cipher not in ciphers:
		print cipher
		print combo
		ciph = cipher
		ciphers.append(cipher)
		
sum = 0
for char in ciph:
	sum += ord(char)
	
print sum