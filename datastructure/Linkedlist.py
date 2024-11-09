class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
        
class LinkedList:
    def __init(self, val):
        
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.next = self.head
        
    def insertFront(self, val):
        
        new_node = ListNode(val)
        
        new_node.next = self.head.next
        new_node.prev = self.head
        
        self.head.next.prev = new_node
        self.head.next = new_node
       
    def insertEnd(self, val):
        
        
        new_node = ListNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        
    def removeEnd(self):
        
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.prev.next = self.tail
        
    def print(self):
        
        cur = self.head.next
        while cur != self.tail:
            print(cur.val, "->")
            cur = cur.next
        print()


class List:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def list_search(self, k):
        curr= self.head.next
        
        while curr != self.tail:
            if curr.val == k:
                return True
            
            curr= curr.next  
        
        return False
    
    def list_insert_idx(self, val, idx):
        
        curr = self.head.next
        new_node = Node(val)
        count = 0
        while curr != self.tail:
            if count == idx:
                new_node.prev = curr
                new_node.next = curr.next
                
                curr.next = new_node
                curr.next.prev = new_node
                
                return 
            count +=1
            curr = curr.next
        return False
    
    def list_insert_head(self, val):
    
        new_node = Node(val)
        
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
            
    def list_insert_tail(self, val):
        
        new_node = Node(val)
        
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
    def list_print(self):
        
        curr = self.head.next
        res = []
        while curr != self.tail:
            res.append(curr.val)
            curr = curr.next
            
        return res
    
    def list_delete(self, idx):
        
        curr = self.head.next
        
        count = 0
        while curr != self.tail:
            if count == idx:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev 
                return
            count += 1
            curr = curr.next
            
    def list_delete_head(self):
        
        
        delete_node = self.head.next
        res = delete_node
        self.head.next = delete_node.next
        delete_node.next.prev = self.head
        
        return res
    