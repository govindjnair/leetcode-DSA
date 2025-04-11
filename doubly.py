class DoublyLinked:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


head = tail = DoublyLinked(1)


# Display O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" <-> ".join(elements))


display(head)


# Insertion at the start O(1)

def insert_at_beg(val, head, tail):
    new_node = DoublyLinked(val, next=head)
    head.prev = new_node
    return new_node, tail


head, tail = insert_at_beg(2, head, tail)
display(head)


# Insert at the end O(1)

def insert_at_end(val, head, tail):
    new_node = DoublyLinked(val, prev=tail)
    tail.next = new_node
    return head, new_node


head, tail = insert_at_end(3, head, tail)
display(head)

head, tail = insert_at_beg(10, head, tail)
display(head)
head, tail = insert_at_end(20, head, tail)
display(head)
