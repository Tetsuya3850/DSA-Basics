def trim_BST(root, L, R):
    # Given a bst and the lowest and highest boundaries, trim the tree so that all its elements lies in [L, R]
    # Time O(N), Space O(H), where N is the num of nodes and H is the height of the tree.
    if not root:
        return root
    if root.val > R:
        return trim_BST(root.left, L, R)
    elif root.val < L:
        return trim_BST(root.right, L, R)
    else:
        root.left = trim_BST(root.left, L, R)
        root.right = trim_BST(root.right, L, R)
        return root
