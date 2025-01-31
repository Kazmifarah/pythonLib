""""
Node class : depicts a node in a linked list
Methods : print(self)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
    def print(self):
        print(self.value, end='->')
        
