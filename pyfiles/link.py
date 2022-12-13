class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, data):
        node=Node(data, self.head)
        self.head=node

    def push(self, data):
        node=Node(self.head, data)
        self.head=node

    def prints(self):
        temp=self.head
        while(temp):
            print(temp.next, end=' ')
            temp=temp.next

a=LinkedList()
a.push(2)
a.push(3)
a.push(4)
a.prints()
