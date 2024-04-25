class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def print_all(self):
        if self.head is None:
            print("linked list is empty")
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
            self.head =new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref 
        if n is None:
            print("node is not present in ll")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not None")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is emtpy")




ll1=Linkedlist()
ll1.add_begin(10)
ll1.add_after(50,10)
ll1.add_before(30,50)
ll1.add_end(100)
ll1.add_begin(20)
ll1.print_all()