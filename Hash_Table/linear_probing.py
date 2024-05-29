
class HashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.table=[None] * capacity

    def _hash(self,key):
        return key% self.capacity
    
    def add(self,key,value):
        index=self._hash(key)
        for i in range(self.capacity):
            new_index=(index+i)%self.capacity
            if self.table[new_index] is None:
                self.table[new_index]=key,value
                return
        print("Hash Table is full")
        
    def disply(self):
        print("Hash Table : ")
        for k,v in enumerate(self.table):
            print(f"{k}:{v}")
        