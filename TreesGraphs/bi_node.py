
class NodePair:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


class BiNode:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


def bi_node(root):
    # Time O(N), Space O(H), where N is the num of nodes and H is the height of the tree.
    return convert(root).head


def convert(root):
    if not root:
        return None

    part1 = convert(root.node1)
    part2 = convert(root.node2)

    if part1:
        part1.tail.node2 = root
        root.node1 = part1.tail

    if part2:
        root.node2 = part2.head
        part2.head.node1 = root

    return NodePair(part1.head if part1 else root, part2.tail if part2 else root)
