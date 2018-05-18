def trimBST(root, L, R):
    # Given a bst and the lowest and highest boundaries, trim the tree so that all its elements lies in [L, R]
    # Time O(N), Space O(H), where N is the num of nodes and H is the height of the tree.
    if not root:
        return root
    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root
