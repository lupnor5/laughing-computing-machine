def minimum_cost(matrix, i = 0, j= 0, lookup = None):
    lookup = {} if lookup is None else lookup
    if (i, j) in lookup: 
        return lookup[(i, j)] 
    m = len(matrix)-1
    n = len(matrix[0])-1

    if i == m and j == n: 
        return matrix[i][j]
    elif i == m: 
        lookup[(i,j)] =  matrix[i][j] + minimum_cost(matrix, i, j+1) #moving down
        return lookup[(i,j)]
    elif j == n:
        lookup[(i,j)] = matrix[i][j] + minimum_cost(matrix, i+1, j) #moving right
        return lookup[(i,j)]
    else:
        lookup[(i,j)] = matrix[i][j] + min(
            minimum_cost(matrix,i, j+1),
            minimum_cost(matrix, i+1, j)
        ) 
        return lookup[(i,j)]

print (minimum_cost([
    [3, 12, 4, 7, 10],
    [6, 8, 15, 11, 4], 
    [19, 5, 14, 32, 21], 
    [1, 20, 2, 9, 7]
]) )