# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.ref=None
# class QueueLinked:
#     def __init__(self):
#         self.front=None
#         self.back=None
    
#     def enqueue(self,value):
#         new_node=Node(value)
#         if self.back is None:
#             self.back,self.front=new_node,new_node
#         else:
#             self.back.ref=new_node
#         self.back=new_node

#     def dequeue(self):
#         if self.back is None:
#             print("queue is empty")
#             return
#         self.front=self.front.ref
#         if self.front is None:
#             self.back=None

#     def display(self):
#         if self.back is None:
#             print("queue is empty")
#             return
#         temp=self.front
#         while temp is not None:
#             print(temp.value)
#             temp=temp.ref

# queue=QueueLinked()
# queue.enqueue(23)
# queue.enqueue(19)
# # queue.display()
# queue.dequeue()
# queue.display()

class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None
class QueNode:
    def __init__(self):
        self.front=None
        self.back=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.back is None:
            self.back,self.front=new_node,new_node
        else:
            self.back.ref=new_node
            self.back=new_node

    def dequeue(self):
        if self.back is None:
            print('queue is empty')
            return
        self.front=self.front.ref
        if self.front is None:
            self.back=None
    def dispaly(self):
        if self.back is None:
            print("queue is empty")
            return
        else:
            temp=self.front
            while temp is not None:
                print(temp.value)
                temp=temp.ref

class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None
class QueueLinked:
    def __init__(self) :
        self.front=None
        self.back=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.back is None:
            self.front,self.back=Node(value),Node(value)
        else:
            self.back.ref=new_node
            self.back=new_node

