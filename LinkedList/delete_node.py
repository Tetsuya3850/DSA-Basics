

def delete_node(node):
    # Time O(1)
    if node.next:
        node.data = node.next.data
        node.next = node.next.next
