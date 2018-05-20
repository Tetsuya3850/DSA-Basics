
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    # Time O(NC), Space O(NC), where N is the num of items and C is the capacity.
    def helper(k, available):
        if k < 0:
            return 0

        if table[k][available] == -1:
            without_curr_item = helper(k-1, available)
            with_curr_item = (0 if available < items[k].weight else (
                items[k].value + helper(k-1, available - items[k].weight)))
            table[k][available] = max(without_curr_item, with_curr_item)
        return table[k][available]
    table = [[-1 for _ in range(capacity + 1)] for _ in items]
    return helper(len(items)-1, capacity)


items = []
wvs = [[5, 60], [3, 50], [4, 70], [2, 30]]
for wv in wvs:
    items.append(Item(wv[0], wv[1]))
print(knapsack(items, 5))
