# euclid-alg

Mitchel Walker
9/9/2019

These two programs, Gcd.py and Euclid.py, are both focused on calculating the Greated Common Divisor (gcd) between two user-given integers. 

***Gcd.py***

A particularly elegant way of finding the gcd is by following the Euclidean Algorithm, which takes advantage of a mathematical theorem that says (a,b) (or the gcd of a and b)
is equal to (b, r1) where a modulo b equals r1 (i.e. r1 is the remainder of a/b). 

Written more explicitly:
	for a = q*b + r1, (a,b) = (b,r1)

From this mathematical theorem we can draw out the steps of the Euclidean Algorithm. It's an iterative process, which takes the following steps:

	(a,b)   = (b,r1)
		= (r1,r2)
		= (r2,r3)
		.
		.
		.
		= (rn,0)
	(a,b)   = rn
	
Here we see that in the iterative and repeating process, the value of a mod b (r1) takes the place of b, and b takes the place of a. Next b mod r1 (r2) takes the place of r1,
and r1 takes the place of b. This process of replacing the larger integer with the smaller integer, and replacing the smaller integer with the remainder is the only process in
the Euclidean Algorithm. These iterative and repetitive processes are the perfect tasks to mandate that our robot servants calculate. Additionally, the process is
naturally recursive, where the base case is a mod b = 0. (This is where b = gcd) This is the process done in Gcd.py. Short, sweet, and simple code that finds the 
gcd of two user-given integers in a fast, recursive process. 






***Euclid.py***

In addition to the process of the Euclidean Algorithm, there is a mathematical identity called Bezout's Identity, which states that (a,b) is equal to the smallest linear combination 
of nonzero a and b. Euclid.py takes a somewhat different approach than Gcd.py to finding the gcd. It's still based on the math of the Euclidean Algorithm, but the end output is
the gcd written as a linear combination of the two user-given integers. According to mathematicians, and one goofy kid at the University of Texas, it's useful to write the gcd
as this linear combination defined in Bezout's Identity. The Extended Euclidean Algorithm deals with finding exactly that. This process can also be found with a recursive
program, but it takes a bit of mathematical savvy to find the relationship between recursive levels.

Consider the following three-step process for finding (a,b) using the Euclidean Algorithm:
	
	(a,b)   = (b,r1)
		= (r1,r2)
		= (r2,0)
		
Written in terms of the remainders:
	
	1.) r1 = a - q1*b
	2.) r2 = b - q2*r1
	3.) 0  = r1 - q3*r2
	
Where, in each case q is the "floor quotient" of the two integers to the right of the equals sign (floor quotient meaning the quotient rounded down to the nearest integer). Let's
refer to the larger of the two numbers as 'x', and the smaller of the two numbers'y'. In each of these equations, let's call the coefficient to x 'm', and the coefficient to y 'n'.
Each of these lines is in the format of the "simple combination", which follows that m = 1, n = q, and the sum of m\*x + n\*y = (x mod y). Given this set of equations,
we want to write the gcd (r2 in this case) as a linear combination of a and b only. 

Let's look at this solution from a recursive point of view. Each step, the recursive function will be called on a new x and y value. The relationship between two adjacent steps is, x2 = y1,
and y2 = (x1 mod y1). This is the basic idea of the Euclidean Algorithm. The base case must be when we've found the gcd, and so equation 3.) can be omitted,
since the gcd is r2. Then, our base case is the situation where (x mod y) = gcd. We also know that (y mod gcd) = 0, so we can define our base case as the situation where
(y mod (x mod y)) == 0. In this case, m = 1, and n = q = (x//y).

We return these m and n values up to the next highest recursive level, which will use then to calculate the next m and n values to pass along. Remember, we want to write the gcd as a linear 
combination of a and b, so let's find the relationship between two adjacent steps, where we can preserve a and b, and cancel out all other variables along the way. If we 
subsitute r1 from equation 1.) into equation 2.) we get 
	
	r2 = b - q2*(a - q1*b). 

However, to make this generalized to fit any case, equation 2 may not be the base case, and it may have any unique coefficients, m2 and n2. We can then rewrite the equation as
	
	r2 = m2*b + n2*(a - q1*b)				(In this case n = -q2)

Combining like terms,
	
	r2 = n2*a + (m2 - n2*q1)*b

From this, we can see that the next m1 and n1 values to pass on up the recursive tree are n2, and (m2 - n2\*q1), respectively. This is the basic identity by which we can create the
recursive program.
	
	-The base case is where (y mod (x mod y)) == 0
	-The base case is a simple combination, and so returns 1 and -(x//y) as m and n, respectively
	-Using m and n passed up from the previous level, each subsequent level passes up (n, m - n*q) where q = x//y of the current recursive level

Finally, the values m and n that are returned by the first level in the recursive loop are the coefficients for the user-given a and b, and they can be used to calculate the gcd. In this
program, though the gdc is found, it is never actually stored in a variable. Instead m and n are used to calculate the gdc.

**Formatting**

Throughout the recursive program, it was assumed that both a and b were positive integers, and that a was larger than b. This is an awfully large constraint to place on our delicate user, so all edge 
cases are handled by performing the recursive function on the absolute value of the user-given integer. Also the larger number is always passed as a, and the smaller always passed as b. This is done
so that the function doesn't need to handle any special cases, and we can manage the edge cases after m and n are calculated. 

There are a few key concepts that are important to mention:
	
	-The gdc of one or more negative numbers is positive
	-The gdc of any number, n, and zero is n
	-The gdc of zero and zero is undefined
	
As such, the program handles the following user-input edge cases before or after the recursive function:
	
	-zero passed as one or more numbers
	-either number is negative
	-number is not an integer - number is rounded down to nearest integer
	-smaller number passed first
	-same number is passed twice
	-gdc is passed as one of the numbers (y%(x%y) will error in this case, since x%y will be zero)


Happy Programming, folks.
