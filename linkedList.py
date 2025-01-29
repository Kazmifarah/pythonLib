import node as N

class LinkedList:
    def __init__(self, value):
        self.head = N.Node(value)
        self.lastNode = self.head
    
    '''
    adds a new Node with specified value and a position
    
    value : value of the node
    
    position : position where the new node needs to be inserted in the linked list
               default is at last position
    '''    
    def addNode(self, value, position=-1):
        
        length = self.length
        
        #case 1 : check if position provided is out of bounds
        if position <-1 or position > length :
            print("Add node : position", position, "provided is out of bounds")
            return
        
        newNode = N.Node(value)
        #case 2 : insert at the end
        if position==-1 or position == length:
            self.lastNode.nextNode = newNode
            self.lastNode = self.lastNode.nextNode
            return
        
        #case 3 : insert at the start
        if position == 0:
            newNode.nextNode = self.head
            self.head = newNode
            return
        
        currentNode=self.head
        count = 1
        #case 4 : insert in middle
        #Traverse to the node just before the position
        while count < position :
            currentNode = currentNode.nextNode
            count += 1
            
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode
        
            
    '''
    returns length of a linked list
    '''
    @property    
    def length(self):
        length = 0
        currentNode = self.head
        while currentNode != None:
            currentNode = currentNode.nextNode
            length+=1

        return length
                    
    def removeNode(self, position=0):
        length = self.length
        
        #case 1: linked list is empty
        if length == 0:
            print("Remove node : Linked list empty")
            return
        
        if position == -1:
            position = length-1
            
        #case 2: check if position provided is out of bounds
        if position <-1 or position >= length :
            print("Remove node : position", position, "provided is out of bounds")
            return
        
        #case 3: Remove the only node in linked list
        if length == 1:
                self.lastNode = None
                self.head = None
                return
            
        #case 4 : 1st node needs to be removed
        currentNode = self.head
        if position == 0:
            self.head=currentNode.nextNode
            return
            
        #case 5 : remove currentNode from middle
        #Traverse to node previous to position
        count=1
        while count < position :
            currentNode = currentNode.nextNode
            count += 1
        currentNode.nextNode = currentNode.nextNode.nextNode
 
    def printLinkedList(self):
        listHead = self.head
        
        if self.head is None:
            print("Linked list empty")
            return

        while listHead is not None:
            listHead.print()
            listHead = listHead.nextNode
        print("None")

    def getElement(self, index):
        
        if self.head is None:
            return None
        
        if index >= self.length or index < -self.length :
            raise IndexError
        
        currentNode = self.head
        count = 0
        
        if index < 0:
            index +=self.length
            
        while count < index:
            count += 1
            currentNode = currentNode.nextNode
        
        return currentNode.value
        
        
        
            