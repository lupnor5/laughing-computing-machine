"""def sum_of_digits(n, sum = 0): 
    if n < 10: 
        return n + sum
    else: 
        return sum_of_digits(n//10, sum + n%10) 
"""


def sumOfDigits(n): 
    if n < 10: 
        return n
    else: 
        return sumOfDigits(n//10) + n%10 

print(sumOfDigits(1234567))     

