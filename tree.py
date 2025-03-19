import treenode

class Tree:
    
    def __init__(self, value):
        self.root = treenode.TreeNode(value)
        
    @property
    def length(self):
        pass
    
    @property
    def level(self):
        pass
    
    def addNode(self, value, index):
        newNode = treenode.TreeNode(value)
        if index < 0 or index >= self.length:
            print("Index {} provided out of bounds".format(index))
            return
        
        if index == 0:
            newNode.children.append(self.root)
            self.root.parent = newNode
            self.root = newNode
            return
        
        
            
    
    def removeNode(self):
        pass
    
    def search(self, index):
        pass