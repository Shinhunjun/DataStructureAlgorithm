memo = [0]*100
#pibonacci

def pibo(x):
    
    if x ==1 :
        return 1
    if x ==2 :
        return 1
    
    if memo[x] != 0:
        return memo[x]
    
    memo[x] = pibo(x-1) + pibo(x-2)
    
    return memo[x]

print(pibo(99))



# 2*n tile problem
memo = [0] * 1000

def tile(n):
    
    if n ==1:
        return 1
    if n==2:
        return 2
    
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = tile(n-1) + tile(n-2)
    
    return memo[n]


print(tile(50))


memo = [0] * 100

def tile2(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = tile2(n-1) + 2* tile2(n-2)
    
    return memo[n]


print(tile2(30))


memo = [0] * 100

def tile3(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    if memo[n] != 0:
        return memo[n]


    result = 3 * tile3(n-2) 
    
    for i in range(3, n):
        if i%2 ==0:
            result += 2* memo[n-i]
    
    memo[n] = result
    return memo[n]

print(tile3(18))