class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
    def print(self):
        print(self.value)
        
class DNode:
    def __init__(self, value):
        self.value = value
        self.previousNode = None
        self.nextNode = None
        
    def print(self):
        print(self.value)