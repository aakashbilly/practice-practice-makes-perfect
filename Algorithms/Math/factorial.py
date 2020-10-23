"""
what is factorial ?
https://www.mathsisfun.com/numbers/factorial.html
https://en.wikipedia.org/wiki/Factorial

5! = 5*4*3*2*1 = 120

0! = 1
1! = 1
n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 3 * 2 * 1

this problem can be implemented in recursive as well as iterative algorithm.
"""
#recursive implementation

def factorialRecursive(n):
    #base case
    if n <=1:
        return 1
    else:
        print(n)
        return n * factorialRecursive(n-1)

#iterative implementation using for loop
def factorialForLoop(n):
    fact = 1
    for i in range(n,0,-1):
        #fact = fact * i
        fact *= i
    return fact

#iterative implemention using while loop
def factorialWhileLoop(n):
    fact = 1
    i = n
    while i>1:
        fact = fact * i
        i-=1
    return fact



