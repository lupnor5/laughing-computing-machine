"""def reverse_iter(s, i): 
    if s == "": 
        return ""
    else: 
        return s[i] + reverse_iter(s, i-1)

def reverse(s): 
    return reverse_iter(s, len(s)-1) 
"""
# a cleaner way to do it

def reverse(s): 
    if s == '': 
        return ''
    else: 
        return reverse(s[1:]) + s[0]
    
print(reverse("lupe"))  