__author__ = "Janna Timmer"

from fractions import Fraction
					
f1 = Fraction(49, 98)
f2 = Fraction(4, 8)

for d in range(11, 100):
	for n in range(10, d):
		reducable = False
		numer = str(n)
		denom = str(d)
		replaced = False
		for digit in denom:
			if digit != '0':
				if digit in numer:
					numer = numer.replace(digit, "")
					denom = denom.replace(digit, "")
					replaced = True
		
		if replaced:
			if len(numer) > 0 and len(denom) > 0:	
				if numer != '0' and denom != '0' and float(numer)/float(denom) == float(n)/float(d):
					print n, "/", d, "=", numer, "/", denom
					if not (d % int(denom) == 0 and n % int(numer) == 0): #i
						for mult in range(2, 20):
							if (n % mult == 0 and d % mult == 0):
								reducable = True
						if not reducable:	
							print n, "/", d, "=", numer, "/", denom
							
print 16.0/64 * 26.0/65 * 19.0/95 * 49.0/98 #0.01 or 1/100

#answer = 100