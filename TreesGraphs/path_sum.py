from collections import defaultdict


def pathSum(root, target):
    # Time O(NlogN), Space O(H), where W is the num of nodes in the tree and H is the height of the tree.
    def helper(node, target, cur):
        if not node:
            return 0
        cur += node.val
        return (1 if cur == target else 0) + helper(node.left, target, cur) + helper(node.right, target, cur)

    if not root:
        return 0
    return helper(root, target, 0) + pathSum(root.left, target) + pathSum(root.right, target)


def pathSumOptimal(root, target):
    # Time O(N), Space O(logN), where W is the num of nodes in the tree.
    def helper(node, cur, target,  path_table):
        if not node:
            return 0
        cur += node.val
        diff = cur - target
        totalPaths = path_table[diff] if diff in path_table else 0

        if cur == target:
            totalPaths += 1

        path_table[cur] += 1
        totalPaths += helper(node.left, cur, target, path_table)
        totalPaths += helper(node.right, cur, target, path_table)
        path_table[cur] -= 1

        return totalPaths

    path_table = defaultdict(int)
    return helper(root, 0, target, path_table)
