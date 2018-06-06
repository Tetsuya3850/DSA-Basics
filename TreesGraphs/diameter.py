def diameter_BTree(root):
    # Time O(N), Space O(H), where N is the num of nodes in tree and H is the height of the tree.
    def helper(node):
        if not node:
            return 0
        l_path, r_path = 0, 0
        if node.left:
            l_path = helper(node.left) + 1
        if node.right:
            r_path = helper(node.right) + 1
        nonlocal max_diameter
        max_diameter = max(max_diameter, l_path + r_path)
        return max(l_path, r_path)

    max_diameter = 0
    helper(root)
    return max_diameter
