class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


four = TreeNode(val=4)
two = TreeNode(val=2)
one = TreeNode(val=1)
three = TreeNode(val=3)
seven = TreeNode(val=7)
six = TreeNode(val=6)
nine = TreeNode(val=9)


four.left = two
four.right = seven
two.left = one
two.right = three
seven.left = six
seven.right = nine


def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)





def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root


pre_order(invertTree(four))

