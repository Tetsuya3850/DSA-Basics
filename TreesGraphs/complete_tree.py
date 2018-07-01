
def is_complete(root, index, number_nodes):
    # Time O(N), Space O(H), where N is the num of nodes and H is the height of the tree.
    if root is None:
        return True
    if index >= number_nodes:
        return False
    return (is_complete(root.left, 2*index+1, number_nodes)
            and is_complete(root.right, 2*index+2, number_nodes)
            )
