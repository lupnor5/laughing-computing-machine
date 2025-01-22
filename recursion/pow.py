# Converting recursive function to tail function

"""
def pow(a, b): 
    if b == 0: 
        return 1
    else: 
        return a * pow(a, b-1)
   """ 
def pow(a, b, accum = 1): 
    if b == 0: 
        return accum
    else: 
        return pow(a, b-1, a * accum)

print(pow(4, 5))