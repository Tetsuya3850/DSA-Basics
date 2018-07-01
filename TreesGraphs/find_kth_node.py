
def find_kth_node(tree, k):
    # Time O(H), where H is the height of the tree.
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1:
            return tree
        else:
            tree = tree.left
    return None
