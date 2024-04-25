class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def print_all(self):
        if self.head is None:
            print("Linked list is empty")
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

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty  so we can't delete nodes")            
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head=None
    
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


ll1=Linkedlist()
ll1.add_begin(20)
ll1.add_begin(10)
ll1.add_end(100)
# ll1.delete_begin()
# ll1.delete_end()
ll1.print_all()