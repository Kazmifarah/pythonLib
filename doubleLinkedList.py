import dnode as D

class DoubleLinkedList:
    def __init__(self, value):
        self.head = D.DNode(value)
        self.tail = self.head
    
    '''
    adds a new Node with specified value and a position
    
    value : value of the node
    
    position : position where the new node needs to be inserted in the linked list
               default is at last position
    '''    
    def addNode(self, value, position=-1):
        
        length = self.length
        
        #case 1 : check if position provided is out of bounds
        if position <-length or position > length :
            print("Add node : position", position, "provided is out of bounds")
            return
        
        newNode = D.DNode(value)
        #case 2 : insert at the end
        if position==-1 or position == length:
            self.tail.nextNode = newNode
            newNode.previousNode = self.tail
            self.tail = newNode
            return
        
        #case 3 : insert at the start
        if position == 0:
            newNode.nextNode = self.head
            self.head.previousNode = newNode
            self.head = newNode
            return
        
        currentNode=self.head
        count = 1
        if position < 0:
            position += length
        #case 4 : insert in middle
        #Traverse to the node just before the position
        while count < position :
            currentNode = currentNode.nextNode
            count += 1
            
        newNode.nextNode = currentNode.nextNode
        newNode.nextNode.previousNode = newNode
        currentNode.nextNode = newNode
        newNode.previousNode = currentNode

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
            
        #case 2: check if position provided is out of bounds
        if position <-1 or position >= length :
            print("Remove node : position", position, "provided is out of bounds")
            return
        
        if position < 0:
            position += length

        #case 3: Remove the only node in linked list
        if length == 1:
                self.tail = None
                self.head = None
                return
            
        #case 4 : 1st node needs to be removed
        currentNode = self.head
        if position == 0:
            currentNode = currentNode.nextNode
            self.head=currentNode
            currentNode.previousNode = None
            return

        #case 5 : last node needs to be removed
        if position == length-1:
            lastNode = self.tail
            lastNode = lastNode.previousNode
            lastNode.nextNode = None
            self.tail = lastNode
            return
            
        #case 6 : remove currentNode from middle
        #Traverse to node previous to position
        count=1
        while count < position :
            currentNode = currentNode.nextNode
            count += 1
        currentNode.nextNode = currentNode.nextNode.nextNode
        currentNode.nextNode.previousNode = currentNode
 
    def printLinkedList(self, reverse = False):
        
        if self.head is None:
            print("Linked list empty")
            return
        
        if reverse :
            listTail = self.tail
            while listTail is not None :
                listTail.print()
                listTail = listTail.previousNode   
        else :
            listHead = self.head
            while listHead is not None:
                listHead.print()
                listHead = listHead.nextNode
        print("None")

    def getElement(self, index):
        
        if self.head is None:
            return None
        
        if index >= self.length or index < -self.length :
            return None
        
        if index < 0:
            index +=self.length

        if index < self.length/2:
            currentNode = self.head
            count = 0
            
            while count < index:
                print("count+", count)
                count += 1
                currentNode = currentNode.nextNode
        
        else :
            currentNode = self.tail
            count = self.length -1
            
            while count > index:
                print("count-", count)
                count -= 1
                currentNode = currentNode.previousNode
        
        return currentNode.value
        
        
        
            