
class HashTable:
    def __init__(self, size):
        self.array = [[] for i in range(size)]
        
    def getHashKey(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum%len(self.array)
    
    def __getitem__(self, key):
        index = self.getHashKey(key)
        
        for element in self.array[index]:
            if element[0] == key:
                return element[1]
        return None
    
    def __setitem__(self, key, value):
        index = self.getHashKey(key)
        length = len(self.array[index])
        for i in range(length):
            if self.array[index][i][0] == key:
                self.array[index][i][1] = value
                return
        self.array[index].append([key, value])
    
    def __delitem__(self, key):
        index = self.getHashKey(key)
        
        length = len(self.array[index])
        for i in range(length):
            if self.array[index][i][0] == key:
                self.array[index].pop(i)
