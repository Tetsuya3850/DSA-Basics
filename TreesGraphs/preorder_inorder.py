from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    # Time O(N), Space O(H), where N is the num of nodes and H is the height of the tree.
    def helper(preorder, l_pre, r_pre, inorder, l_in, r_in, lookup):
        if l_pre > r_pre or l_in > r_in:
            return None
        root = preorder[l_pre]
        inorder_root_i = lookup[root]
        left_tree_size = inorder_root_i - l_in
        root_node = TreeNode(root)
        root_node.left = helper(
            preorder, l_pre+1, l_pre + left_tree_size, inorder, l_in, inorder_root_i-1, lookup)
        root_node.right = helper(
            preorder, l_pre + left_tree_size + 1, r_pre, inorder, inorder_root_i+1, r_in, lookup)
        return root_node

    lookup = defaultdict()
    for i in range(len(inorder)):
        lookup[inorder[i]] = i
    return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, lookup)
