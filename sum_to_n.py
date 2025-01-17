# Converting a recursive function to a tail-recursive function

"""def sum_to_n(n): 
    if n == 0: 
        return 0
    else: 
        return n + sum_to_n(n - 1)
   """
# Tail recursive - won't fill call stack

def sum_to_n(n, accum = 0): 
    if n == 0: 
        return accum
    else:
        return sum_to_n(n-1, accum + n) 
     

print(sum_to_n(10))    #must be 55