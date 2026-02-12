# traversing the linked list 

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

# function to traverse/ print 

def printLinkedList(head):
    curr = head

    while curr!=None:
        print(curr.data, end= " ")
        curr = curr.next 


# create the linked_list and make sure that
a = Node(3)
b = Node(5)
c = Node(7)

head =a                  
a.next = b 
b.next = c        

printLinkedList(head)