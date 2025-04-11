class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


# def display(head):
#     curr = head
#     nodes = []
#     while curr:
#         nodes.append(str(curr.val))
#         curr = curr.next
#
#     print("->".join(nodes))


three = ListNode(3)
two = ListNode(2)
zero = ListNode(0)
four = ListNode(4)

three.next = two
two.next = zero
zero.next = four
four.next = two


def hasCycle(head):
    dummy = ListNode()
    dummy.next = head
    slow = fast = dummy

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return True

    return False


print(hasCycle(three))
