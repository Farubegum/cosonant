def value(sab): 
	if (sab == 'I'): 
		return 1
	if (sab == 'V'): 
		return 5
	if (sab == 'X'): 
		return 10
	if (sab == 'L'): 
		return 50
	if (sab == 'C'): 
		return 100
	if (sab == 'D'): 
		return 500
	if (sab == 'M'): 
		return 1000
	return -1

def romanToDecimal(str): 
	re = 0
	j  = 0
	while (j < len(str)): 
		sam1 = value(str[j]) 
		if (j+1 < len(str)): 
			sam2 = value(str[j+1]) 
			if (sam1 >= sam2): 
				re = re + sam1 
				j = j + 1
			else: 
				re = re + sam2 - sam1 
				j = j + 2
		else: 
			re = re + sam1 
			j = j + 1
	return re 
J = input()
print(romanToDecimal(J)) 
