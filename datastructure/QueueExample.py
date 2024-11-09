from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
        
# we are checking if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
        #return not self.items
        
    # you can push the element 
    def enqueue(self, item):
        self.items.append(item)
    # delete the top of the stack
    def dequeue(self):
        return self.items.popleft()
    #the  element of the stack
    def peek(self):
        return self.items[0]
    # size of the stack
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()
    
    
    print(q1.is_empty())
    q1.enqueue(5)
    q1.enqueue(6)
    q1.enqueue(64)
    print(q1)
    
    q1.dequeue()
    print(q1)
    print(q1.size())
    print(q2.size())
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(64)
    print(q2.size())


    
        
    
    
   