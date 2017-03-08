class BinarySearchTreeNode:
    def __init__(self,value):
        self.data=value
        self.right=None
        self.left=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        node=BinarySearchTreeNode(value)
        cur=self.root
        if(self.root==None):
            self.root=node

        else:
            while True:
                if(cur.data<=value):
                    if(cur.right==None):
                        cur.right=node
                        return
                    else:
                        cur=cur.right
                elif(cur.data>value):
                    if(cur.left==None):
                        cur.left=node
                        return
                    else:
                        cur=cur.left

    def inorderTraversal(self):
        def traino(tree):
            if(tree!=None):
                traino(tree.left)
                print(tree.data)
                traino(tree.right)
        traino(self.root)

    def postorderTraversal(self):
        def trapost(tree):
            if(tree!=None):
                trapost(tree.left)
                trapost(tree.right)
                print(tree.data)
        trapost(self.root)

    def preorderTraversal(self):
        def trapreo(tree):
            if(tree!=None):
                print(tree.data)
                trapreo(tree.left)
                trapreo(tree.right)
        trapreo(self.root)

    





t=BinarySearchTree()
t.insert(20)
t.insert(12)
t.insert(25)
t.insert(16)
t.insert(6)
t.insert(9)
t.insert(44)
##t.inorderTraversal()
t.postorderTraversal()
##t.preorderTraversal()
                     
                     
                     

         
             
