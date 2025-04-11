class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


five = Node(5)
four = Node(4)
three = Node(3)
two = Node(2)
one = Node(1)

five.next = four
four.next = three
three.next = two
two.next = one
head = five


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(elements))


def reverse(head):
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return display(prev)


display(head)
reverse(head)