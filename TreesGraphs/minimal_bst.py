# Create a BST with minimal height from a sorted array with unique integers.

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right

def minimal_bst(A):
    def minimal_bst_helper(A, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = BinaryTreeNode(A[mid])
        root.left = minimal_bst_helper(A, start, mid-1)
        root.right = minimal_bst_helper(A, mid+1, end)
        return root
    return minimal_bst_helper(A, 0, len(A) - 1)

print (minimal_bst([2, 4, 5, 7, 11, 13, 17]))
