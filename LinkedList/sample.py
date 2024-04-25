class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def printall(self):
        if self.head is None:
            print("linkedd list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data == x :
                break
        if n in None:
            print("node is empty")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node



    





ll=Linkedlist()
ll.add_begin(10)
ll.add_after(20,10)
ll.add_end(100)
ll.printall()