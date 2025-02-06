import doubleLinkedList as DLL

class Stack:
    def __init__(self, value):
        self.items = DLL.DoubleLinkedList(value)
    
    def push(self, value):
        self.items.addNode(value, 0)
    
    def pop(self):
        self.items.removeNode()
    
    def peek(self):
        return self.items.getElement(0)
    
    def print(self):
        self.items.printLinkedList()
    
    @property
    def length(self):
        return self.items.length   