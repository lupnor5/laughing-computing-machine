def hasAdjacentDuplicates(s, i=1): 
    if i >= len(s): 
        return False
    elif s[i] == s[i-1]: 
        return True
    else: 
        return hasAdjacentDuplicates(s, i+1)
    

print(hasAdjacentDuplicates("lalalalala"))
print(hasAdjacentDuplicates("Programming"))

