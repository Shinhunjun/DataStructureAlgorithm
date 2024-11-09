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