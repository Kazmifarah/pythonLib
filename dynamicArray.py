
class DynamicArray:
    
    capacity = 10
    
    def __init__(self):
        self.array = [None]* DynamicArray.capacity
        self.freeIndex = 0
    
    @property
    def length(self):
        return self.freeIndex
    
    def printArray(self):
        print(self.array[0:self.length])
            
    def insert(self, value, index = -1):
        
        if self.freeIndex == len(self.array):
           self.__resize()
        
        arrayLength = len(self.array)
        if index < -1 or index >= arrayLength:
            print("Index", index, "is out of bounds")
            print("Please enter a number between 0 and ", arrayLength)     
            return
        
        if index == -1:
            self.array[self.freeIndex] = value
        else : 
            self.__shiftArrayItems(index)
            self.array[index] = value
        self.freeIndex += 1
        
    def remove(self, index =0):

        if self.length == 0:
            print("Array empty. Nothing to remove")
            return
        
        arrayLastIndex = self.length-1
        if index<0 or index > arrayLastIndex:
            print("Index", index, "is out of bounds")
            print("Please enter a number between 0 and ", arrayLastIndex)     
            return
        
        for i in range(index,arrayLastIndex):
            self.array[i] = self.array[i+1]
        self.freeIndex -= 1
            
    def __resize(self):
        newSize = self.length + DynamicArray.capacity
        newArray = [None] * newSize
        
        for i in range(0, self.length):
            newArray[i] = self.array[i]
        
        self.array = newArray
        
    def __shiftArrayItems(self, index):
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1] 