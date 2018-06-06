
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def successor_node(node):
    # Find the in-order successor node in a bst. You may assume that each node has a link to its parent.
    # Time O(H), Space O(1), where H is the height of the tree.
    if node.right:
        next_node = node.right
        while next_node.left:
            next_node = next_node.left
        return next_node
    else:
        cur_node = node
        next_node = cur_node.parent
        while next_node and next_node.left != cur_node:
            cur_node = next_node
            next_node = next_node.parent
        return next_node


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


A = BinaryTreeNode(314)
B = BinaryTreeNode(6)
I = BinaryTreeNode(6)
A.left = B
A.right = I
B.parent = A
I.parent = A
C = BinaryTreeNode(271)
F = BinaryTreeNode(561)
J = BinaryTreeNode(2)
O = BinaryTreeNode(271)
B.left = C
B.right = F
I.left = J
I.right = O
C.parent = B
F.parent = B
J.parent = I
O.parent = I
D = BinaryTreeNode(28)
E = BinaryTreeNode(0)
G = BinaryTreeNode(3)
K = BinaryTreeNode(1)
P = BinaryTreeNode(28)
C.left = D
C.right = E
F.right = G
J.right = K
O.right = P
D.parent = C
E.parent = C
G.parent = F
K.parent = J
P.parent = O
H = BinaryTreeNode(17)
L = BinaryTreeNode(401)
N = BinaryTreeNode(257)
G.left = H
K.left = L
K.right = N
H.parent = G
L.parent = K
N.parent = K
M = BinaryTreeNode(641)
L.right = M
M.parent = L

print(successor_node(A.right.right.right))
