# Question 1 (15 pt.) Order statistics: Write codes for Rand-Select (with linear expected running time)
# and Select (with linear worst-case running time). Test your two programs with an input array that is a
# random permutation of A = {1, 2, 3, …, 99, 100}.

import random

def random_partition(arr, p, r):
    #choosing the random pivot and swap with the last element
    pivot_idx = random.randint(p,r)
    arr[pivot_idx] , arr[r] = arr[r], arr[pivot_idx]
    pivot = arr[r]
    
    #partition the array around the pivot
    i = p - 1 
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    
    arr[i + 1], arr[r] = arr[r], arr[i+1]
    
    return i + 1 #return the pivot's final index
       
    
def random_select(arr, p, r, i):
    
    #if the subarray has only one element, return.(base case)
    if p == r:
        return arr[p]
    
    #randomly partition the array and get the pivot's position
    q = random_partition(arr, p, r)
    k = q - p + 1 #position of the pivot element in the subarray
    
    
    # check if the pivot is the i-th smallest element
    if i == k:
        return arr[q]
    
    elif i < k:
        return random_select(arr, p, q-1, i) #recur on the left sub-array
    else: 
        return random_select(arr, q+1, r, i-k) #recur on the right sub-array
    
def select_partition(arr, p, r, pivot_idx):
    arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]
    pivot = arr[r]
    
    # partition the array around the pivot
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[r] = arr[r], arr[i+1] 
    return i + 1 #return the pivot's final index


def select(arr, p, r, i):
    # adjust the array length to be a multiple of 5 by removing small elements from the start
    while (r - p + 1) % 5 != 0:
        # find the minimum element int the current subarray
        for j in range(p+1, r+1):
            if arr[p]> arr[j]:
                arr[p], arr[j] = arr[j], arr[p]                
        if i == 1:
            return arr[p]        
        p += 1
        i -= 1
    # partitioning the array into groups of 5, find medians of eaxh group    
    g = (r - p + 1) // 5 # number of group
    medians = []   
    for j in range(g):
        start = p + 5 * j
        end = start + 5 
        group_sorted = sorted(arr[start : end]) # sort each group
        medians.append(group_sorted[2]) # append the median of each group
        
# Finding median of median.
    median_of_medain = (
        select(medians, 0, len(medians)-1 , len(medians)//2 )
        if len(medians) > 1 else medians[0]
    )

# partition arr[p:r+1] around the pivot
    pivot_idx = arr.index(median_of_medain, p, r+1)
    pivot_idx = select_partition(arr, p, r, pivot_idx)
    
    k = pivot_idx - p + 1
    
    if i == k:
        return arr[pivot_idx]
    elif i < k:
        return select(arr, p, pivot_idx -1, i)
    else: 
        return select(arr, pivot_idx +1, r, i - k)
        
A = list(range(1, 101))
random.shuffle(A)
print(A)

random_number = random.choice(A)

print(f"The selected order :{random_number} the number the function return: ", random_select(A,0, len(A)-1, random_number))   
#print(f"The selected order :{random_number} the number the function return: ", select(A,0, len(A)-1, random_number))     
        



def randomized_partition(A,p,r):
    
    pivot = random.randint(p,r)
    A[pivot], A[r] = A[r], A[pivot]
    j = p -1
    for i in range(1,r):
        if A[i] <= A[r]:
            j +=1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1
    
def random_select(A,p,r,i):
    
    if p == r:
        return A[p]
    
    q = randomized_partition(A,p,r)
    
    k = q - p +1
    
    if i == k :
        return A[i]
    
    if i < k:
        return random_select(A,p,q-1,i)
    else: 
        return random_select(A,q+1, r, i-k)
        