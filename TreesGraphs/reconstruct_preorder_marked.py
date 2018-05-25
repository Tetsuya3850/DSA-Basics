
class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def reconstruct_preorder(preorder):
    # Time O(N), where N is the num of nodes in tree.
    def helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None

        left_subtree = helper(preorder_iter)
        right_subtree = helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
    return helper(iter(preorder))
