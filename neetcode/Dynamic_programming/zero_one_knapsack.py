
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


weight = [1, 2, 3]
profit = [6, 10, 12]
capacity = 5

print(dfs(weight, profit, capacity))
# Expected output: 22 (Items with weight 2 and 3 are included)