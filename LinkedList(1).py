class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,value):
        node=Node(value)
        if (self.head==None):
            self.head=node
            self.tail=self.head

        else:
            self.tail.next=node
            self.tail=self.tail.next

    def search(self,value):
        cur=self.head
        while (cur!=None):
            if (cur.data==value):
                return True
            cur=cur.next
        return False

    def delete(self,value):
        cur=self.head
        if (self.head.data==value):
            cur.next=self.head
            cur.next=None
        else:
            while (cur.next!=None):
                if(cur.next.data==value):
                   if (cur.next==self.tail):
                       self.tail = cur
                       cur.next=None
                   else:
                       cur.next=cur.next.next
                   return
                    
                cur=cur.next

    
                       
            
                

l=LinkedList()
l.insert("a")
print(l.search("a"))
l.insert("b")
l.insert("g")
l.delete("b")
print(l.search("b"))
        
