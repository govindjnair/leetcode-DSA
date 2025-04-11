class SinglyLinked:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


head = SinglyLinked(1)
A = SinglyLinked(3)
B = SinglyLinked(5)
C = SinglyLinked(7)
head.next = A
A.next = B
B.next = C


# traverse O(n)

curr = head
while curr:
    print(curr)
    curr = curr.next


# Display the linked list O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(elements))


display(head)


# Search for a node O(n)

def search(head, val):
    curr = head
    while curr:
        if val == curr.value:
            return True
        curr = curr.next
    return False


print(search(head, 2))

