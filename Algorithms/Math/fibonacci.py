"""
What Is The Fibonacci Sequence?

https://en.wikipedia.org/wiki/Fibonacci_number
https://www.mathsisfun.com/numbers/fibonacci-sequence.html
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the
recurrence relation

Fn = Fn-1 + Fn-2 with seed values

F0 = 0 and F1 = 1.

Given a number n, print n-th Fibonacci Number.
Examples:

Input  : n = 2
Output : 1

Input  : n = 9
Output : 34

Write a function int fib(int n) that returns Fn.
For example, if n = 0, then fib() should return 0.
If n = 1, then it should return 1.
For n > 1, it should return Fn-1 + Fn-2

For n = 9
Output:34
"""

#Method 1 ( Use recursion )
#A simple method that is a direct recursive 
#implementation mathematical recurrence relation given above.
#Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential. so this is a bad implementation.
#Extra Space: O(n) if we consider the function call stack size, otherwise O(1)
def getNthFib(n):
    if n < 0:
        return print("wrong input!")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)
