#this program takes two numbers as input parameters and returns the linear combination that sums to their greatest common divisor
#math is based on the euclidian algorithm

'''
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
'''

def euclidian(a,b):
	#this function returns the z-linear combination coefficients of given numbers a and b

	#run algorithm on the absolute value of given numbers
	x = max(abs(a),abs(b))
	y = min(abs(a),abs(b))
	return euclidianHelper(x,y)


def euclidianHelper(x,y):
	#this functions returns the m and n coefficients of the linear combination solution
	#m is the coefficient of the larger magnitude number
	#base case - where x % y is the gcd
	if y%(x%y) == 0:
		return (1, -(x//y))
	else:
		(m, n) = euclidianHelper(y, x%y)
		q = x//y
		return (n, m - n*q)


def printCombination(x,y):
	#prints the linear combination and computes the gcd from m and n values
	#m and n are calculated for abs value of both x and y
	print("Linear Combination of Greatest Common Divisor:\n", end = '\t')
	#first check if x or y == 0
	if x == 0 and y == 0:
		print('undefined')
		return
	if x == 0:
		a = y/abs(y)
		print("%s = 0 + %s*%s" % (a*y,a,y))
		return
	elif y == 0:
		a = x/abs(x)
		print("%s = 0 + %s*%s" % (a*x,a,x))
		return
	#check if x == y
	if abs(x) == abs(y):
		if x > 0:
			print("%s = 0*%s + 1*%s" % (x,y,x))
		elif y > 0:
			print("%s = 0*%s + 1*%s" % (y,x,y))
		else:
			#both are negative 
			print("%s = 0*%s + -1*%s" % (-x,y,x))
		return

	#all other cases
	(m,n) = euclidian(x,y)
	#swap m & n if y > x
	if abs(x) < abs(y):
		m,n = n,m
	#correct for negative numbers
	if x < 0:
		m *= -1
	if y < 0:
		n *= -1
	#print the combination
	f = m*x + n*y
	print("%s = %s*%s + %s*%s" % (f,m,x,n,y))


def main():
	a = int(input("input 1st number: "))
	b = int(input("input 2nd number: "))
	#print("%d, %d" % (a,b))
	printCombination(a,b)

main()