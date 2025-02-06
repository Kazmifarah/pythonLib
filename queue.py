from collections import deque

class Queue:
    def __init__(self):
        self.deque = deque()
        
    def enqueue(self, value):
        self.deque.appendleft(value)
    
    def dequeue(self):
        return self.deque.pop()
    
    def getFront(self):
        return self.deque[-1]
    
    def getRear(self):
        return self.deque[-0]
    
    def print(self):
        print(self.deque)
        
    @property
    def length(self):
        return len(self.deque)
