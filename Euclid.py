#this program takes two numbers as input parameters and returns the linear combination that sums to their greatest common divisor
#math is based on the euclidian algorithm
import math


def euclidian(a,b):
	#this function returns the z-linear combination coefficients of given numbers a and b

	#run algorithm on the absolute value of given numbers
	x = max(abs(a),abs(b))
	y = min(abs(a),abs(b))
	return euclidianHelper(x,y)


def euclidianHelper(x,y):
	#this functions returns the m and n coefficients of the linear combination solution
	#m is the coefficient of the larger magnitude number
	#base case - where x % y is the gcd, so y % (x%y) must be zero
	
	#check if x%y is zero to prevent an error
	if x%y == 0:
		return (1,-(x//y - 1))
	if y%(x%y) == 0:
		return (1, -(x//y))
	else:
		(m, n) = euclidianHelper(y, x%y)
		#q is the floor quiotient of x and y
		q = x//y
		return (n, m - n*q)


def hasZeroes(x,y):
	#this function handles if a zero is passed as a or b
	if x == 0 and y == 0:
		print('undefined')
		return True
	if x == 0:
		a = y//abs(y)
		print("%s = 0 + %s*%s" % (a*y,a,y))
		return True
	elif y == 0:
		a = x//abs(x)
		print("%s = 0 + %s*%s" % (a*x,a,x))
		return True
	return False


def areEqual(x,y):
	#this program handles the case where the absolute value of x and y are equal
	if abs(x) == abs(y):
		if x > 0:
			print("%s = 0*%s + 1*%s" % (x,y,x))
		elif y > 0:
			print("%s = 0*%s + 1*%s" % (y,x,y))
		else:
			#both are negative 
			print("%s = 0*%s + -1*%s" % (-x,y,x))
		return True
	return False


def handleNegatives(m,n,x,y):
	#this function both handles if x or y was given as negative, and also if b > a
	#it returns the potentially modified m and n values

	#swap m & n if y > x
	if abs(x) < abs(y):
		m,n = n,m
	#correct for negative numbers
	if x < 0:
		m *= -1
	if y < 0:
		n *= -1
	return (m,n)


def printCombination(x,y):
	#prints the linear combination and computes the gcd from m and n values
	#m and n are calculated for abs value of both x and y
	print("\nGreatest Common Divisor as a Linear Combination:\n", end = '\t')
	#first check if x or y == 0
	if hasZeroes(x,y):
		return

	#check if x == y
	if areEqual(x,y):
		return

	#calculate m and n for positive x & y - and where x>y
	(m,n) = euclidian(x,y)
	
	#handle negatives and where b > a
	(m,n) = handleNegatives(m,n,x,y)

	#print the combination
	f = m*x + n*y
	print("%s = %s*%s + %s*%s" % (f,m,x,n,y))


def main():
	#Ask for each number - ensure that they are integers
	a = int(input("input 1st number: "))
	b = int(input("input 2nd number: "))
	
	printCombination(a,b)


main()
