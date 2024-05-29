class heap:
    def __init__(self) -> None:
        self.heap=[]
    def parent(self,index):
        return (index-1)//2
    def leftchild(self,index):
        return 2*index+1
    def rightchild(self,index):
        return 2*index+2
    def heapify_up(self,index):
        parent=self.parent(index)
        if index>0 and self.heap[index]>self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
    def heapify_down(self,index):
        left=self.leftchild(index)
        right=self.rightchild(index)
        largest=index 
        if left < len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest=right
        if largest != index :
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self.heapify_down(largest)  

    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root =self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root 
    def pee_max(self):
        return self.heap[0] if self.heap else None
    
