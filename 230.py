class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


five = TreeNode(5)
three = TreeNode(3)
six = TreeNode(6)
two = TreeNode(2)
four = TreeNode(4)
one = TreeNode(1)

five.left = three
five.right = six
three.left = two
three.right = four
two.left = one


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)


# in_order(five)

k = 3
count = k
answer = 0


def kth(node):
    global count, answer
    if not node:
        return
    kth(node.left)
    if count == 1:
        answer = node.val
    count -= 1

    if count > 0:
        kth(node.right)



kth(five)
print(answer)
