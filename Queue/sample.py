# def sorting(arr):
#     for i in range(1,5):
#         if i != arr[i]:
#             return False
#     return True
# list=[1,2,3,4,5]
# k=sorting(list)
# print(k)

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.ref=None

# class StackNode:
#     def __init__(self):
#         self.top=None
    

#     def pop(self):
#         if self.top is None:
#             print("stack is ")


k="The quick brown fox jumps over the lazy gigantic dog"
j=[]




class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None
class StackLinked:
    def __init__(self):
        self.top=None
    
    def push(self,value):
        new_node=Node(value)
        if self.top is None:
            self.top=Node(value)
        else:
            new_node.ref=self.top
            self.top=new_node

    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            self.top=self.top.ref 

    def display(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.ref  
            
    def reverse(self,stirng):
        for char in stirng:
            self.push(char)
        k=""
        while self.top is None:
            k+=self.top.value
            self.pop()
        return k