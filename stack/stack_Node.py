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
            print("is empty")
            return
        else:
            self.top=self.top.ref

    def dispaly(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.ref

    def reverse(self, string):
        for char in string:
            self.push(char)
        reverse_string = ""
        while self.top is not None:
            reverse_string += self.top.value
            self.pop()
        return reverse_string
    
list=StackLinked()
# list.push(23)
# list.push(21)
# list.pop()
# list.dispaly()

# str="munavar"
# reversed=list.reverse(str)
# print(reversed)


class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.ref=None
    
class StackNode:
    def __init__(self) -> None:
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
    def dispay(self):
        temp=self.top
        while self.top is not None:
            print(temp.value)
            temp=temp.ref
    def reverse(self,string):
        for char in string:
            self.push(char)
        reverse=""
        while self.top is not None:
            reverse+=self.top.value
            self.pop()
        return reverse