class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

def isPalindrome(word):
    s1=Stack()
    string=[]
    for i  in word:
        string.append(i)
    for j in word:
        s1.push(j)
    reverse=[]

    while (not s1.isEmpty()):
        reverse.append(s1.pop())

    if (string==reverse):
        return True
    else:
        return False

##print(isPalindrome("dog"))
##print(isPalindrome("madam"))

def paranthesis(equation):
    p1=Stack()
    for i in equation:
        if (i=="(" or i=="[" or i=="{"):
            p1.push(i)

        elif(i==")" or i=="]" or i=="}"):
            if (not p1.isEmpty()):
                p2=p1.pop()
                if (i==")" and p2=="("):
                    pass
                elif (i=="]" and p2=="["):
                    pass
                elif (i=="}" and p2=="{"):
                    pass
                else:
                    return False
            else:
                return False

    if (not p1.isEmpty()):

        return False

    return True

print(paranthesis("[3x+5(4x-2)]"))
print(paranthesis("[3x+5(4x-2]"))            
    








        

    


