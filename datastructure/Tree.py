from collections import deque    
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
        self.prev = None
        
      
class Tree:
    
    def __init__(self):
        self.root = None
        
    def search(self, k):
        curr = self.root
        
        while curr is not None:
            if curr.val > k :
                curr = curr.left
            elif curr.val < k :
                curr = curr.right
            else:
                return curr
            
        return None

    def search_recur(self, node, k):
        
        if node == None or node.val == k:
            return node

        if node.val > k :
            self.search_recur(node.left, k)
            
        else: 
            self.search_recur(node.right, k)

    def tree_min(self, node):
        
        while node.left is not None:
            node = node.left
            
        return node
            
    def tree_max(self, node):
        
        while node.right is not None:
            node= node.right
            
        return node
        
    def tree_successor(self, node): 
        #오른쪽 노드가 있다면 거기서 가장 작은 거
        # 없다면 왼쪽노드인데... 자기가 오른쪽 자식이면 오른쪽 자식이 아닐때까지 부모를 타고 올라가서 그걸 리턴해야함
        
        if node.right is not None:
            return self.tree_min(self, node.right)

        else: 
            node_parent = node.parent
            while node_parent is not None and node_parent.right == node:
                node = node_parent
                node_parent = node_parent.parent
                
            return node_parent
        
    def tree_insert(self, val):
        # 새 노드 만들고 curr, parent 포인터 지정해서 curr로 new node 가 들어갈 장소 찾고, 찾은 후 Parent, new_node 연결  그 이후 parent의 왼쪽 오른쪽 자식 여부 결정
        new_node = Node(val)
        curr_parent = None
        curr = self.root
        
        while curr is not None:
            curr_parent = curr
            
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        new_node.parent = curr_parent
        if curr_parent is None:
            self.root = new_node
            
        if curr_parent.val > new_node.val:
            curr_parent.left = new_node
        else:
            curr_parent.right = new_node            

    def transplant(self, delete, new):
        # 삭제하려는 노드와 그 삭제하는 노드에 붙이려는 노드,
        # 삭제하는 노드의 부모가 없으면 그냥 루트가 붙이는 노드에 이어지면 됌
        # 삭제되는 노드가 만약 부모의 왼쪽 자식이면 부모의 왼쪽에 붙여주면되고
        # 반대면 반대로
        
        # 새로 붙이는 노드가 존재한다면 새로붙이는 노드의 부모를 설정해주면 됌
        
        # 트리구조에서는 부모입장에서 왼,오른 따지고 자식입장에서도 부모 포인터를 설정해줘야함.
        
        if delete.parent is None:
            self.root = new
        else:    
            if delete.parent.left == delete :
                delete.parent.left = new
            else:
                delete.parent.right = new
                
        if new is not None:
            new.parent = delete.parent
    
    def delete(self, node):
        
        if node.left is None:
            self.transplant(node, node.right)
            
        elif node.right is None:
            self.transplant(node, node.left)
        
        else:   
            right_min = self.tree_min(node.right)
            
            if node.right != right_min:
                self.transplant(right_min, right_min.right)
                right_min.right = node.right
                node.right.parent = right_min

                
            right_min.left = node.left                
            node.left.parent = right_min

            
            self.transplant(node, right_min)
       


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
    


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.val)
        inorder(node.right)
        
    return node
        
    
def preorder(node):
    if node is not None:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
        
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
    
    
def tree_search(node, k):
    
    if node is None and node.val == k :
        return node
    
    if node.val < k:
        return tree_search(node.right, k)
    
    else: 
        return tree_search(node.left, k)
    
    
def tree_search_iterative(node, k):
    
    while node is not None and node.val != k:
        
        if node.val < k:
            node = node.right
            
        else: 
            node = node.left

    return node        

def tree_min(node):
    while node.left is not None:
        node = node.left
        
    return node

def tree_max(node):
    while node.right is not None:
        node = node.right
        
    return node

def tree_successor(node):
    
    if node.right is not None:
        return tree_min(node.right)
    
    else:
        y = node.parent
        
        while y is not None and y.right == node:
            node = y
            y= y.parent
            
        return y
    
def tree_insert(root, val):
    
    new_node = Node(val)
    curr = root
    curr_parent = None

    while curr is not None:
        curr_parent = curr
        
        if curr.val > val:
            curr = curr.left
        else:
            curr = curr.right
            
            
    if curr_parent is None:
            root = new_node
    else: 
        if curr_parent.val > val:
            curr_parent.left = new_node
        else: 
            curr_parent.right = new_node
            
    new_node.parent = curr_parent
    
    return root

def transplant(root, u, v):
    if u.parent is None:
        root = v
    else:
        if u.parent.right == u:
            u.parent.right = v
        else: 
            u.parent.left = v
            
    if v is not None:
        v.parent = u.parent
        
def tree_delete(root, z):
    
    if z.left == None:
        transplant(root, z, z.right)
        
    elif z.right == None:
        transplant(root, z, z.left)
        
        
    else: 
        # z의 오른쪽에서 가장 작은 노드를 찾고
        # 그 노드가 z의 바로 오른쪽 노드가 아니라면
        # 그 노드의 오른쪽과 그 노드의 부모를 붙이고
        # 그 노드의 오른쪽으로 z의 오른쪽을 붙여주고
        # 그 노드의 왼족으로 z 의 왼족을 붙이고
        # 부모 연결한다
        m = tree_min(z.right)
        
        if z.right != m:
            transplant(root, m, m.right)
            m.right = z.right
            m.right.parent = m 
        
        m.left = z.left
        m.left.parent = m
        
        
#Give a recursive version of the TREE-INSERT procedure.

def insert(root, v):
    
    if root is None: 
        return Node(v)
    
    if root.val < v:
        insert(root.right, v)
        
    else: 
        insert(root.left, v)
        
    return root