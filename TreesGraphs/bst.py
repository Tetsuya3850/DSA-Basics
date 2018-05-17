class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Time O(logN), Space O(1), where N is the num of nodes in bst.
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            parent = None
            curr = self.root
            while curr:
                parent = curr
                if data == curr.data:
                    return False
                elif data < curr.data:
                    curr = curr.left
                else:
                    curr = curr.right
            if data < parent.data:
                parent.left = BinaryTreeNode(data)
            else:
                parent.right = BinaryTreeNode(data)

    def find(self, data):
        # Time O(logN), Space O(1), where N is the num of nodes in bst.
        curr = self.root
        while curr:
            if data == curr.data:
                return True
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, data):
        # Time O(logN), Space O(1), where N is the num of nodes in bst.
        curr = self.root
        parent = None
        while curr and curr.data != data:
            parent = curr
            curr = curr.left if data < curr.data else curr.right
        if not curr:
            return False
        key_node = curr
        if key_node.right:
            r_key_node = key_node.right
            r_parent = key_node
            while r_key_node.left:
                r_parent = r_key_node
                r_key_node = r_key_node.left
            key_node.data = r_key_node.data
            if r_parent.left == r_key_node:
                r_parent.left = r_key_node.right
            else:
                r_parent.right = r_key_node.right
        else:
            if self.root == key_node:
                self.root = key_node.left
            else:
                if parent.left == key_node:
                    parent.left = key_node.left
                else:
                    parent.right = key_node.left

    def print_inorder(self):
        # Time O(N), Space O(1), where N is the num of nodes in bst.
        def print_inorder_helper(root):
            if not root:
                return
            print_inorder_helper(root.left)
            print(root.data, end=' ')
            print_inorder_helper(root.right)
        print_inorder_helper(self.root)
        print()

    def get_min(self):
        # Time O(logN), Space O(1), where N is the num of nodes in bst.
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def get_max(self):
        # Time O(logN), Space O(1), where N is the num of nodes in bst.
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data


bst = BinarySearchTree()
bst.insert(50)
bst.insert(32)
bst.insert(56)
bst.insert(16)
bst.insert(48)
bst.insert(52)
bst.insert(60)
bst.insert(7)
bst.insert(20)
bst.insert(56)
print(bst.find(17))
bst.delete(54)
print(bst.root.right.data)
bst.print_inorder()
print(bst.get_min())
print(bst.get_max())
