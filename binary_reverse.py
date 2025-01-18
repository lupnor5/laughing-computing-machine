# This is a more efficient way to reverse a string reversing half string every time
def binary_reverse(s):
    if len(s) == 1: 
        return s
    else: 
        middle = len(s)//2
        left = s[0:middle]
        right = s[middle:]
        return binary_reverse(right) + binary_reverse(left)  

print(binary_reverse('123456789'))