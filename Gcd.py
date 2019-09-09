#this program takes two integers from the user and prints the 

def gcd(a,b):
	x = max(abs(a),abs(b))
	y = min(abs(a),abs(b))
	return gcd_helper(x, y)


def gcd_helper(a,b):
	#this function returns the greatest common divisor of a and b (a greater than b)
	if a % b == 0:
		return b
	else:
		return gcd(b, a%b)

def main():
	#take user input
	a = int(input("input 1st number: "))
	b = int(input("input 2nd number: "))

	#print greatest common divisor
	print("Greatest Common Divisor: " + str(gcd(a,b)))

main()