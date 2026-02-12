class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# print linked list
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next


# delete first node
def deleteFirst(head):

    head = head.next
    return head


def deleteLast(head):
    curr = head
    while curr.next.next!= None:
        curr= curr.next
    
    curr.next = None

    return head

def deleteKth(head, k):

    curr = head
    for i in range(k-1):
        curr = curr.next

    curr.next = curr.next.next

    return head

# create linked list: 4 -> 5 -> 6 -> 3 -> 7 -> 1
a = Node(4)
b = Node(5)
c = Node(6)
d = Node(3)
e = Node(7)
f = Node(1)

head = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print("Original:", end=" ")
printLinkedList(head)


# delete first
head = deleteFirst(head)
print("\nAfter delete first:", end=" ")
printLinkedList(head)

# deleter last
head = deleteLast(head)
print("\nAfter delete last:", end=" ")
printLinkedList(head)


k = 2
head = deleteKth(head, k)
print("\nAfter delete k=2:", end=" ")
printLinkedList(head)