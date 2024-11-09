class Heap:
    
    def __init__(self):
        pass
    
    def max_heapify(self, arr, n, i):
        # n = len(arr)  
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            arr[i] , arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, n, largest)
        
    def build_heap(self, arr, n):
        
        # n = len(arr)
        for i in range((n-1)//2, -1, -1):
            self.max_heapify(arr, n, i)

    def heap_sort(self, arr, n):
        
        self.build_heap(arr, n)
        # n = len(arr)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.max_heapify(arr, i, 0)

        return arr
    
    def heap_max(self, arr):
        if len(arr) == 0:
            return "heap underflow"
        self.build_heap(arr,len(arr))
        return arr[0]
    
    def heap_max_extract(self, arr):
        
        maximum = self.heap_max(arr)
        n = len(arr)
        arr[0] = arr[n-1]
        self.max_heapify(arr, n-2, 0)
        
        return maximum
    
    def heapify_up(self, arr, i):
        
        parent = (i-1) // 2
        
        while i > 0:
            if arr[parent] < arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
                parent = (i-1) // 2
            else: 
                break
            
    def heap_insert(self, arr, x):
        arr.append(x)
        self.heapify_up(arr, len(arr)-1)
        #log n 의 시간복잡도

    def max_heap_increase_key(self, arr, i, new_val):
        if new_val < arr[i]:
            raise ValueError("New Key is smaller than the current key")
        
        arr[i] = new_val
        self.heapify_up(arr, i)
        
class PriorityQueue:
    
    def __init__(self):
        self.heap = Heap()
        self.items = []
        
    def is_empty(self):
        
        return len(self.items) == 0
    
    def enqueue(self, val): 
        
        self.items.append(val)
        self.heap.heap_insert(self.items, val)
        # self.items이라는 배열에 heap_insert를 한다.
        
    def dequeue(self):
        
        if not self.is_empty():
            maximum = self.heap.heap_max_extract(self.items)
        else: 
            return "Priority Queue is empty"
        
    def peek(self):
        
        if not self.is_empty():
            return self.heap.heap_max(self.items)
        else:
            return "Priority Queue is empty"
        
        
    def size(self):
        
        return len(self.items)
    
    def __str__(self):
        
        return str(self.items())
        

            
class Stack:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        
        return len(self.items) == 0
    
        
    def push(self, val):
        
        self.items.append(val)
        
    def pop(self):
        if self.is_empty():
            return "UnderFlow"
        
        last = self.items.pop()
        
        return last

class Queue:
    
    def __init__(self):
        self.list = List()
        
    
    def is_empty(self):
        
        return self.list.head.next == self.list.tail
        
    def enqueue(self, val):
        
        self.list.list_insert_tail(val)
        
    def dequeue(self):
        
        if not self.is_empty():
            
            delete_node =self.list.list_delete_head()
            return delete_node
        else: 
            return "node is empty"

    def peek(self):
        
        if not self.is_empty():
            return self.list.head.next
        
        else:
            return "node is empty"
    def __str__(self):
        # 큐의 내용을 문자열로 반환
        # List 클래스의 list_print 메서드를 사용하여 연결 리스트의 값을 반환
        return str(self.list.list_print())   
       
class Queue2:
    
    def __init__(self):
        self.items = deque()
        
    def is_empty(self):
        return len(self.items) == 0 
    
    def enqueue(self, val):
        self.items.append(val)
        
    def dequeue(self):
        if not self.is_empty():
            
            out = self.items.popleft()
            return out
        else: 
            return "queue is empty"
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        
        return self.items[0]
    

    def __str__(self):
        return str(self.items)

class Stack2:
    
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return len(self.items) == 0
      
    def push(self, val):
        
        self.items.append(val)
        
    def pop(self):
        
        out = self.items.pop()
        
        return out
    
    def __str__(self):
        return str(self.items)
      
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def search (self, k):
        if self.head == None:
            return "None"
        
        curr = self.head
        
        while curr:
            if curr.val == k:
                return curr
            curr = curr.next
        
        return None
    
    def prepend(self, k):
        new_node = Node(k)
        
        new_node = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node
            
        self.head = new_node
    
    def list_insert(self, node_insert, node):
        
        node_insert.next = node
        node_insert.prev = node.prev
        
        if node.prev is not None:
            node.prev.next = node_insert
        
        node.prev = node_insert
        
    def list_delete(self, node):
        
        
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
            
        if node.next is not None:
            node.next.prev = node.prev
            
    


def merge_sort(arr):
    
    n = len(arr)
    
    if n == 1:
        return
    
    q = n // 2 
    # 0,1,2,3 n=4 4//2 =2 -> 2 
    # 0, 1, 2 n=3 3//2 =1 -> 1
    # 0, 1 n=2 2//2 =1 
    
    
    left = arr[:q]
    right = arr[q:]
    
    merge_sort(left)
    merge_sort(right)
    
    i=j=k=0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return arr


def max_heapify(arr, n , i):
    largest = i
    left = 2*i +1
    right = 2*i +2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)
        
def build_max_heap(arr, n):
    for i in range((n-1)//2, -1, -1):
        max_heapify(arr, n, i)
        
def heap_sort(arr, n):
    
    build_max_heap(arr, len(arr))
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i , 0)
    return arr       

def maxheap_max(arr):
    n = len(arr)
    
    if n < 1:
        return "heap underflow"
    return arr[0]

def heapmax_extract(arr):
    n= len(arr)
    build_max_heap(arr, n)
    maximum = maxheap_max(arr)
    arr[n-1], arr[0] = arr[0], arr[n-1]
    max_heapify(arr, n-2, 0)
    
    return maximum
    

def maxheap_increase_key(arr, curr, val):
    
    if arr[curr] > val:
        return "current key is bigger than new one"
    
    arr[curr] = val
    curr_parent = (curr-1) // 2
    while curr > 0 and arr[curr_parent] < arr[curr]:
        arr[curr], arr[curr_parent] = arr[curr_parent], arr[curr]
        curr = curr_parent
        curr_parent = (curr_parent - 1) // 2 
               
def maxheap_insert(arr, val):
    
    arr.append(-float('inf'))
    maxheap_increase_key(arr, len(arr)-1, val)
    