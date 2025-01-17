# Turning a recursive function to a tail-recursive function
# 9617086242 profe Juan Carlos Lizama Zavaleta
"""
def getMin(arr, i = 0): 
    if i == len(arr): 
        return float('inf')
    else: 
        return min(arr[i], getMin(arr, i + 1))
"""

def getMin(arr, i = 0, min_num = float('inf')):
    if i == len(arr): 
        return min_num
    else:
        return getMin(arr, i + 1, min(arr[i], min_num))
    


print(getMin([7, 11, 12, 45, 4, 6, 7]))
