class node:
    def __init__(self, data):
        self.data=data
        self.nxt=None

class listmanager:

    def __init__(self):
        self.head=None

    def push(self, data):
        new_node= node(data)
        new_node.nxt= self.head
        self.head=new_node 
        print(f"the data {data} is pushed into the list")
    
    def pop(self):
        if self.head==None:
            print(" warning !!!!! the singly linked list is empty")
        
        else:
            popvar=self.head
            self.head=self.head.nxt
            print(f"the data {popvar} is poped from list")
    
    def display(self):
        if self.head ==None:
            print("Can't print empty list")
        else:
             currentvar=self.head
             while currentvar is not None:
                 print(currentvar.data, end="--->")
                 currentvar=currentvar.nxt
             print(None)


op='Y'
l=listmanager()
while op == 'Y':
    print(" which operation do u wnat to run ")
    
    x= int(input("1.Push 2.Pop 3.Display "))
    if x==1:
        data=int(input("enter push data:"))
        l.push(data)
    elif x==2:
        l.pop()
    elif x==3:
        l.display()
    else:
        print("invalid opinion")
    op= 'n'
        
        
    


       


        
    

            


