class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


A = ListNode(1)
B = ListNode(2)
C = ListNode(4)

A.next = B
B.next = C

D = ListNode(1)
E = ListNode(3)
F = ListNode(4)

D.next = E
E.next = F


def display(head):
    curr = head
    nodes = []
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next

    print("->".join(nodes))


display(A)
display(D)


def merge(list1, list2):
    d = ListNode()
    curr = d
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next

        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

    curr.next = list1 if list1 else list2

    return d.next


merged = merge(A, D)
display(merged)






