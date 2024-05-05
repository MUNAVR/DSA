class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.ref=None

class HashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity

    def _hash(self,key):
        return hash(key)*self.capacity
        
    def insert(self,key,value):
        index=self._hash(key)

        if self.table[index] is None:
            self.table[index]=Node(key,value)
            self.size+=1
        else:
            current=self.table[index]
            while current:
                if current.key==key:
                    current.value=value
                    return
                current=current.ref
            new_node=Node(key,value)
            new_node.ref=self.table[index]
            self.table[index]=new_node
            self.size+=1

    def search(self,key):
        index=self._hash(key)
        current=self.table[index]
        while current:
            if current.key ==  key :
                return current.value
            current=current.ref
            
    def remove(self,key):
        index=self._hash(key)
        pre=None
        current=self.table[index]

        while current:
            if current.key==key:
                if pre:
                    pre.ref=current.ref
                else:
                    self.table[index]=current.ref
                    self.size-=1
                return
            pre=current
            current=current.ref
        



