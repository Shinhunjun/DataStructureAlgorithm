def unique_path(m,n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    
    return dp[m-1][n-1]

print(unique_path(3,3))


def dfs(m,n):
    memo = [([-1] * m ) for  j in range(n)]
    
    def memo_helper(i,j):
        if i== (m-1) or j == (n-1):
            return 1
        if i >=m or j>= n:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        memo[i][j] = memo_helper(i,j+1) + memo_helper(i+1,j)
        
        return memo[i][j]
    
    return memo_helper(0,0)

print(dfs(3,3))