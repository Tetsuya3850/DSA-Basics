
def level_order(root):
    # Time O(N), Space O(L), where N is the num of nodes in tree and L is the max num of nodes in a level.
    if not root:
        return []
    level = [root]
    result = []
    while level:
        curr_level_num = []
        next_level = []
        for node in level:
            curr_level_num.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        result.append(curr_level_num)
        level = next_level
    return result
