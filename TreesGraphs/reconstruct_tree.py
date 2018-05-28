from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reconstruct_preorder_inorder(preorder, inorder):
    # All keys are unique.
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


def reconstruct_preorder_marked(preorder):
    # Time O(N), where N is the num of nodes in tree.
    def helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None

        root = TreeNode(subtree_key)
        root.left = helper(preorder_iter)
        root.right = helper(preorder_iter)
        return root
    return helper(iter(preorder))


def valid_serialization(preorder):
    # Time O(N), where N is the num of nodes in tree.
    def helper(iter):
        root_key = next(iter, None)
        if root_key == None:
            nonlocal result
            result = False
            return
        elif root_key == '#':
            return
        helper(iter)
        helper(iter)

    result = True
    preorder_ar = preorder.split(',')
    it = iter(preorder_ar)
    helper(it)
    if next(it, None) != None:
        result = False
    return result


def reconstruct_preorder_bst(preorder):
    def helper(preorder, start, end):
        if start > end:
            return None
        root = preorder[start]
        transition_point = start + 1
        while transition_point < len(preorder) and preorder[transition_point] > preorder[start]:
            transition_point += 1
        root_node = TreeNode(root)
        root_node.left = helper(preorder, start+1, transition_point-1)
        root_node.right = helper(preorder, transition_point, end)
        return root_node

    return helper(preorder, 0, len(preorder)-1)


print(reconstruct_preorder_bst([43, 23, 37, 29, 31, 41, 47, 53]).val)
