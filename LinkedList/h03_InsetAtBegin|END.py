# insertion at the begining of thhe liNKED LIST 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# insertion of teh begining 

def insertAtBegin(head, data):
    newNode = Node(data)

    newNode.next = head 
    head = newNode

    return head

def insertAtEnd(head, data):
    newNode = Node(data)
    curr = head 
    while curr.next!= None:
        curr= curr.next

    curr.next = newNode
    return head


def PrintList(head):
    curr = head
    while curr!= None:
        print(curr.data, end = "")
        curr= curr.next


# putting the value in the linked list 
a = Node(5)
b = Node(3)
c= Node(7)

head = a
a.next = b 
b.next = c

print("Before:", end=" ")
PrintList(head)

# insert 4 at beginning
head = insertAtBegin(head, 4)

print("\nAfter:", end=" ")
PrintList(head)

# insert 1 at end
head = insertAtEnd(head, 1)

print("\nAfter inserting at end:", end=" ")
PrintList(head)