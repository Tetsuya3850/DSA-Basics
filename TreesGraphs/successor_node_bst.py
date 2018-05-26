
def successor_node_bst(tree, k):
    # Time O(H), where H is the height of the tree.
    next_so_far = None
    while tree:
        if tree.data > k:
            next_so_far = tree
            tree = tree.left
        else:
            tree = tree.right
    return next_so_far
