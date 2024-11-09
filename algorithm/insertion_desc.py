
def insertion_sort_desc(arr):
    
    for i in range(len(arr)):
        key = arr[i]
        j = i -1
        
        while j>=0 and arr[j]< key:
            arr[j+1] = arr[j]
            arr[j] = key
            j -= 1
        
    return arr

example = [1, 2, 3, 4, 5 ,6, 7]

print(insertion_sort_desc(example))