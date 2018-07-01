
def is_subtree(t1, t2):
    # Time O(N), Space O(N), where N is the num of nodes in t1.
    preorder_t1 = get_preorder(t1)
    preorder_t2 = get_preorder(t2)
    return preorder_t2 in preorder_t1


def get_preorder(root):
    # Time O(N), where N is the num of nodes in tree.
    def helper(node):
        nonlocal A
        if not node:
            A.append('X')
            return
        A.append(str(node.data) + " ")
        helper(node.left)
        helper(node.right)

    A = []
    helper(root)
    return "".join(A)


def is_subtree_alternative(t1, t2):
    # Time O(N + kM), Space O(log(N)), where N, M is the num of nodes in t1, t2.
    # And k is the num of nodes in t2 that match t1's root.
    def is_subtree_helper(t1, t2):
        if not t1:
            return False
        elif t1.data == t2.data and match_tree(t1, t2):
            return True
        return is_subtree_helper(t1.left, t2) or is_subtree_helper(t1.right, t2)
    if not t2:
        return True
    return is_subtree_helper(t1, t2)


def match_tree(t1, t2):
    # Time O(M), Space O(log(M)), where M is the num of nodes in t2.
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.data != t2.data:
        return False
    else:
        return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = BinaryTreeNode(314)
root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(6)
root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(271)
root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(3)
root.right.left.right = BinaryTreeNode(1)
root.right.right.right = BinaryTreeNode(28)
root.left.right.right.left = BinaryTreeNode(17)
root.right.left.right.left = BinaryTreeNode(401)
root.right.left.right.right = BinaryTreeNode(257)
root.right.left.right.left.right = BinaryTreeNode(641)

print(is_subtree(root, root.left.right))
print(is_subtree_alternative(root, root.left.right))
