# Input: text1 = "cat", text2 = "crabt" 
# Output: 3 


# recursion : O(2^(m+n))
def lcs1(s1, s2):
    
    def dfs(i,j):
        
        if i == len(s1) or j == len(s2):
            return 0
        
        if s1[i] == s2[j]:
            return dfs(i+1,j+1) + 1
        
        else:
            return  max(dfs(i+1, j), dfs(i, j+1))
        
    return dfs(0,0)
        
text1 = "cat"
text2 = "crabt" 

print(lcs1(text1,text2))

# memoization : O(m+n)

def lcs2(s1, s2):
    
    memo = {}
    
    def dfs(i,j):
        if i == len(s1) or j == len(s2):
            return 0
        
        if (i,j) in memo:
            return memo[(i, j)]
        
        if text1[i] == text2[j]:
            memo[(i,j)] = 1 + dfs(i+1,j+1)
        else: 
            memo[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            
        return memo[(i,j)]
        
    return dfs(0,0)

print(lcs2(text1, text2))


# Top-Down Dynamic programming O(M*N)
def lcs3(s1,s2):
    
    def dfs():
        
        M, N = len(s1), len(s2)
        
        dp = [[0] * (N+1) for _ in range(M+1)]
        
        for i in range(1,M+1):
            for j in range(1, N+1):
                
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[M][N]
    
    return dfs()

print(lcs3(text1,text2))