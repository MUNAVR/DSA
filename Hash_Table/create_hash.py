class Hash_table:
    def __init__(self) :
        self.max=100
        self.arr=[None]* self.max

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max

    def add(self,key,value):
        h=self.get_hash(key)    
        self.arr[h]=value
    
    def get(self,key):
        h=self.get_hash(key)
        print(self.arr[h])


#python standerd operators


    def __setitem__(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
    
    def __getitem__(self,key):
        h=self.get_hash(key)
        print(self.arr[h])

    def __delitem__(self, key) :
        h=self.get_hash(key)
        self.arr[h]=None

result=Hash_table()
result.get_hash("munavar")
result.add("munavar", 439)
result.get("munavar")
result

result["march 6"]= 123
result["march 7"]=500
result["march 6"]

del result["march 7"]
result["march 7"]

