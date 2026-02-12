# linked list creation and all the operation in this 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
a = Node(5)              #create nodes
b = Node(3)
c = Node(7)

head =a 
a.next = b               # connect the nodes
b.next = c

print(a.data, "->", a.next.data, "->",a.next.next.data)


