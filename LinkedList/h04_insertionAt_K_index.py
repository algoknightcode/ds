# insetion at the kth index

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

# for printing the linked_list

def printLinkedList(head):
    curr = head
    while curr!=None:
        print(curr.data, end=" ")
        curr= curr.next

# insert at the kth index

def InsertAtK(head,data,k):
    newNode = Node(data)

    curr = head
    for i in range(k-1):  # becuse i want at position 3 but we start the index from the 0 that why
        curr = curr.next

    newNode.next = curr.next
    curr.next = newNode

    return head


# create linked list: 4 -> 5 -> 3 -> 7 -> 1
a = Node(4)
b = Node(5)
c = Node(3)
d = Node(7)
e = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

print("Before:", end=" ")
printLinkedList(head)

# call function
k = 2
head = InsertAtK(head, 6, k)

print("\nAfter:", end=" ")
printLinkedList(head)