class HashTbale:
    def __init__(self,size):
        self.size=size
        self.table=[None]* self.size
    def get_hash(self,key):
        return key%self.size
    def get_hash2(self,key):
        return 5 -(key%5)
    def insert(self,key,value):
        index=self.get_hash(key)
        index2=self.get_hash2(key)
        
        while self.table[index] is not None:
            index=(index+self.get_hash2)%self.size
            if index==self.size:
                print("Hash Table is full")
        self.table[index]=(key,value)

    def get(self,key):
        index=self.get_hash(index=key)
        index2=self.get_hash2(key)
        
        while self.table[index] is not None:
            if self.table[index][0]==key:
                return self.table[index][1]
            index=(index+self.get_hash2)%self.size
            if index==self.size:
                return None
        return None
            