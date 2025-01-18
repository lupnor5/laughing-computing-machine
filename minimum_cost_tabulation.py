def minimum_cost_path(matrix): 
    n = len(matrix)
    m = len(matrix[0])
    i, j = 0, 0
    dp = [[0] * m for _ in range(n)]

    for i in range(0, m):
        for j in range(0, n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif j == 0:
                dp[j][i] = matrix[j][i] + dp[j][i-1] 
            elif i == 0:
                dp[j][i] = matrix[j][i] + dp[j-1][i]     
            else: 
                dp[j][i] = matrix[j][i] + min(dp[j-1][i], dp[j][i-1])
    return dp[n-1][m-1]       
    

print (minimum_cost_path([
    [3, 12, 4, 7, 10],
    [6, 8, 15, 11, 4], 
    [19, 5, 14, 32, 21], 
    [1, 20, 2, 9, 7]
]) )