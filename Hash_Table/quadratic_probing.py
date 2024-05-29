class HashTable:
    def __init__(self,size) :
        self.size=size
        self.table=[None] * self.size

    def get_hash(self,key):
        return key%self.size
    
    def insert(self,key,value):
        index=self.get_hash(key)
        i=0
        while self.table[index] is not None:
            index=(index+i**2)%self.size
            i+=1
            if i ==self.size:
                print("Hash Table is full")
        self.table[index]=(key,value)
    
    def get(self,key):
        index=self.get_hash(key)
        i=1
        while self.table[index] is not None:
            if self.table[index][0]==key:
                return self.table[index][1]
            index=(index+i**2)%self.size
            i+=1
        