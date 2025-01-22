def countOccurrences(arr, num, i = 0, counter = 0): 
    if i == len(arr): 
        return counter
    else:
        if arr[i] == num: 
            return countOccurrences(arr, num, i + 1, counter + 1)
        else: 
            return countOccurrences(arr, num, i + 1, counter)
        

print(countOccurrences([4, 2, 7, 4, 4, 1, 2], 4))
