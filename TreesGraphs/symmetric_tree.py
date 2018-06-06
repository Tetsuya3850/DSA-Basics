
def is_symmetric(root):
    def helper(left, right):
        # Time O(N), Space O(H), where N is the num of nodes in tree and H is the height of the tree.
        if not left and not right:
            return True
        elif left and right:
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        else:
            return False

    return not root or helper(root.left, root.right)
