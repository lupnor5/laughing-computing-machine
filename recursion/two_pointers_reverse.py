def two_pointer_reverse(s, left, right): 
    if left > right: 
        return 
    else: 
        s[left],s[right] = s[right],s[left] 
        two_pointer_reverse(s, left+1, right-1)

def reverse(s): 
    s = list(s)
    two_pointer_reverse(s, 0, len(s)-1)
    return "".join(s)

print(reverse('123456789'))        