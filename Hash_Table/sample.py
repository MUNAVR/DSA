# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.ref=None
    
        

# class HashTable:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size

#     def get_hash(self,key):
#         return key%self.size
    
#     def linear(self,key,value):
#         index=self.get_hash(key)
#         for i in range(self.size):
#             new_index=(index+i)%self.size
#             if self.table[new_index] is None:
#                 self.table[new_index]=key,value
#                 return
            
#     def seperate(self,key,value):
#         index=self.get_hash(key)

#         if self.table[index] is None:
#             self.table[index]=Node(key,value)
#         else:
#             current=self.table[index]
#             while current:
#                 if current.key==key:
#                     current.value=value
#                     return
#                 current=current.ref
#             new_node=Node(key,value)
#             new_node.ref=self.table[index]
#             self.table[index]=new_node


#     def insert(self,key,value):
#         index=self.get_hash(key)
#         self.table[index]=key,value

#     def get(self,key):
#         index=self.get_hash(key)
#         return self.table[index]
    
#     def disaply(self):
#         print("Hash Table")
#         for i,j in enumerate(self.table):
#             print(f"{i}:{j}")


# hash=HashTable(10)
# hash.insert(3,100)
# hash.insert(4,300)
# # j=hash.get(3)
# # hash.disaply()

# hash.linear(9,200)
# hash.linear(9,700)


# hash.seperate(6,600)
# hash.seperate(6,400)
# k=hash.get(6)
# print(k)
# hash.disaply()

# class Node:
#     def __init__(self,value,key):
#         self.key=key
#         self.value=value
#         self.ref=None
# class Hashtabe:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
#     def get_hash(self,key):
#         return key%self.size
    
#     def insert(self,key,value):
#         index=self.get_hash(key)
#         self.table[index]=key,value
#     def get(self,key):
#         index=self.get_hash(key)
#         return self.table[index]
#     def display(self):
#         for i,j in enumerate(self.table):
#             print(f"{i}:{j}")
        
#     def seprete(self,key,value):
#         new_node=Node(key,value)
#         index=self.get_hash(key)
#         if self.table[index] is None:
#             self.table[index]=Node(key,value)
#         else:
#             current=self.table[index]
#             while current:
#                 if current.key==key:
#                     current.value=value
#                     return
#                 current=current.ref
#             new_node.ref=self.table[index]
#             self.table[index]=new_node


class Node:
    def __init__(self,key,value):
        self.value=value
        self.key=key
        self.ref=None

class HashTable:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.table=[None]*self.capacity
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.capacity
    def get_hash1(self,key):
        return key%self.capacity
    
    def insert(self,key,value):
        index=self.get_hash1(key)
        self.table[index]=key,value
    def linear(self,key,value):
        index=self.get_hash1(key)
        for i in range(self.capacity):
            new_index=(index+i)%self.capacity
            if self.table[new_index] is None:
                self.table[new_index]=key,value
                return
    def seperate(self,key,value):
        index=self.get_hash1(key)
        if self.table[index] is None:
            self.table[index]=Node(key,value)
        else:
            current=self.table[index]
            while current:
                if current.key ==key:
                    current.value = value
                    return
                current=current.ref
            new_node=Node(key,value)
            new_node.ref=self.table[index]
            self.table=new_node
    def quadratic(self,key,value):
        index=self.get_hash1(key)
        i=0
        while self.table[index] is not None:
            index=(index+i**2)%self.capacity
            i+=1
            if i==self.capacity:
                print("table is full")
        self.table[index]=key,value
    def get(self,key):
        index=self.get_hash1(key)
        return self.table[index]
    
    def get_Item(self,key):
        index=self.get_hash1(key)
        current=self.table[index]
        while current:
            if current.key==key:
                return current.value
            current=current.ref
    def disaply(self):
        for i ,j in enumerate(self.table):
            print(f"{i}:{j}")


hash=HashTable(20)
# hash.insert(12,200)
# hash.linear(12,300)
# hash.quadratic(12,600)
hash.seperate(2,400)
hash.seperate(2,500)
k=hash.get(12)
# print(k)
p=hash.get_Item(12)
print(p)
# hash.disaply()


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

# two dimension
