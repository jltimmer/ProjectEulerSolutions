__author__ = "Janna Timmer"

count = 1
for c1 in range(201):
	calc = 1*c1
	if calc == 200:
		count += 1
	if calc >= 200:
		break
	for c2 in range(101):
		calc = 1*c1 + 2*c2
		if calc == 200:
			count += 1
		if calc >= 200:
			break
		for c5 in range(41):
			calc = 1*c1 + 2*c2 + 5*c5
			if calc == 200:
				count += 1
			if calc >= 200:
				break
			for c10 in range(21):
				calc = 1*c1 + 2*c2 + 5*c5 + 10*c10
				if calc == 200:
					count += 1
				if calc >= 200:
					break
				for c20 in range(11):
					calc = 1*c1 + 2*c2 + 5*c5 + 10*c10 + 20*c20
					if calc == 200:
						count += 1
					if calc >= 200:
						break
					for c50 in range(5):
						calc = 1*c1 + 2*c2 + 5*c5 + 10*c10 + 20*c20 + 50*c50
						if calc == 200:
							count += 1
						if calc >= 200:
							break
						for c100 in range(3):
							calc = 1*c1 + 2*c2 + 5*c5 + 10*c10 + 20*c20 + 50*c50 + 100*c100
							if calc == 200:
								count += 1
							if calc >= 200:
								break
								
print count