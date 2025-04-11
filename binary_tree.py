from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


# recursive pre order traversal DFS Time O(n), space O(n)
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)


# Time O(n), space O(n)
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)


# Time O(n) and space O(n)

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

    # pre_order(A)


# pre_order(A)
# in_order(A)
# post_order(A)

# iterative approach , pre-order traversal o(n)

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


# pre_order_iterative(A)

# level order traversal BFS
def level_order(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# level_order(A)


# check value DFS
def search(node, target):
    if not node:
        return False
    if node.value == target:
        return True
    return search(node.left, target) or search(node.right, target)

# print(search(A, 10))


# BST

#       5
#    1    8
#  -1 3  7 9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# in_order(A2)


def search_bst(node, target):
    if not node:
        return False

    if node.value == target:
        return True

    if target < node.value:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


print(search_bst(A2, 8))


