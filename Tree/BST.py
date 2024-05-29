class BST:
    def __init__(self,key):
        self.lchild=None
        self.key=key
        self.rchild=None

    def insertion(self,key):
        if self.key is None:
            self.key=key
            return 
        if self.key==key:
            return 
        if self.key >key:
            if self.lchild:
                self.lchild.insertion(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insertion(key)
            else:
                self.rchild=BST(key)
    def search(self,key):
        if self.key==key:
            print("data is founded")
            return
        if self.key >key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("not founded")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("not founded")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=" ")

bst=BST(23)
bst.insertion(12)
bst.insertion(33)
bst.preorder()
        