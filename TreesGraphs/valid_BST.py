
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def valid_BST(root):
    # Check whether a binary tree is a binary search tree.
    # Time O(N), Space O(H), where W is the num of nodes in the tree and H is the height of the tree.
    def valid_BST_helper(root, mini, maxi):
        if root is None:
            return True
        if root.data < mini or root.data > maxi:
            return False
        return valid_BST_helper(root.left, mini, root.data - 1) and valid_BST_helper(root.right, root.data + 1, maxi)
    return valid_BST_helper(root, float('-inf'), float('inf'))


root = BinaryTreeNode(50)
root.left = BinaryTreeNode(32)
root.right = BinaryTreeNode(54)
root.left.left = BinaryTreeNode(16)
root.left.right = BinaryTreeNode(48)
root.right.left = BinaryTreeNode(52)
root.right.right = BinaryTreeNode(60)
root.left.left.left = BinaryTreeNode(7)
root.left.left.right = BinaryTreeNode(20)
root.right.right.left = BinaryTreeNode(56)
print(valid_BST(root))
