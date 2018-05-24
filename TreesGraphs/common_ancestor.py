def common_ancestor(tree, node0, node1):
    # Compute the lowest common ancestor of two nodes in a binary tree.
    # Time O(N), Space O(H), where N is the num of nodes in tree and H is the height of the tree.
    def common_ancestor_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)
        left_result = common_ancestor_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result
        right_result = common_ancestor_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result
        num_target_nodes = left_result.num_target_nodes + \
            right_result.num_target_nodes + \
            int(tree is node0) + int(tree is node1)
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return common_ancestor_helper(tree, node0, node1).ancestor


class Status:
    def __init__(self, num_target_nodes, ancestor):
        self.num_target_nodes = num_target_nodes
        self.ancestor = ancestor


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = BinaryTreeNode(314)
root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(6)
root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(271)
root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(3)
root.right.left.right = BinaryTreeNode(1)
root.right.right.right = BinaryTreeNode(28)

print(common_ancestor(root, root.left.left, root.left.right))


def LCA_bst(tree, s, b):
    # Least Common Ancestor for bst.
    # Time O(H), where H is the height of the tree.
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree
