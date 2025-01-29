""""
DNode class : depicts a node in a double linked list
Methods : print(self)
"""
class DNode:
    def __init__(self, value):
        self.value = value
        self.previousNode = None
        self.nextNode = None
        
    def print(self):
        print(self.value, end='<->')