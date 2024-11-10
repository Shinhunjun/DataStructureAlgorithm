
#solution 1
#brute force O(2^(m+n))

def dfs(weight, profit, capacity):
    def dfsHelper(i, weight, profit, capacity):
        if i == len(profit):
            return 0
        
        skip = dfsHelper(i+1, weight, profit, capacity)
        
        include = 0
        new_cap = capacity - weight[i]
        
        if new_cap >= 0:
            include = profit[i] + dfsHelper(i+1, weight, profit, new_cap)
            
            
        return max(skip, include)
    
    return dfsHelper(0, weight, profit, capacity)

#solution 2 

def momoization(weight, profit, capacity):
    
    cache = [[-1] * (capacity+1) for _ in range(len(profit))]
    
    return memohelper(0, weight, profit, capacity, cache)


def memohelper(i , weight, profit, capacity, cache):
    
    if i == len(profit):
        return 0
    
    if cache[i][capacity] != -1:
        return cache[i][capacity]
    
    cache[i][capacity] = memohelper(i+1, weight, profit, capacity, cache)
    
    new_cap = capacity - weight[i]
    
    if new_cap >=0:
        include = profit[i] + memohelper(i+1, weight, profit, new_cap, cache)
        
        cache[i][capacity] = max(cache[i][capacity], include)
        
    return cache[i][capacity]
    


def dp(weight, profit, capacity):
    
    M, N = len(profit), capacity
    
    dp = [[0]* (N+1) for _ in range(M)]
    
    for c in range(N+1):
        if weight[0] <= c:
            dp[0][c] = profit[0]
            
    for i in range(1,M):
        for c in range(N+1):
            skip = dp[i-1][c]
            
            new_cap = c - weight[i]
            include = 0 
            
            if new_cap >= 0:
                include = profit[i] + dp[i-1][new_cap]
            
            dp[i][c] = max(include, skip)
            
    return dp[M-1][N]
            
    

            
    


weight = [1, 2, 3]
profit = [6, 10, 12]
capacity = 5

# print(dfs(weight, profit, capacity))
# # Expected output: 22 (Items with weight 2 and 3 are included)

print(dp(weight, profit, capacity))