# With quarters, dimes, nickels and pennies, calculate the ways of making a change.

def make_change(change, coins):
    change_table = [[[] for _ in range(change + 1)] for _ in coins]
    for i in range(len(coins)):
        change_table[i][coins[i]].append([coins[i]])

    for j in range(len(coins)):
        for k in range(1, change + 1):
            if j >= 1 and change_table[j - 1][k]:
                change_table[j][k].extend(change_table[j - 1][k])
            if k >= coins[j] and change_table[j][k - coins[j]]:
                for without_changes in change_table[j][k - coins[j]]:
                    change_table[j][k].append(without_changes + [coins[j]])

    return change_table[-1][-1]

print (make_change(30, [25, 10, 5, 1]))



def num_change(change, coins):
    pre_num_change = [1] + [0] * change
    num_change = [1] + [0] * change

    for i in range(1, change + 1):
        if i >= coins[0]:
            pre_num_change[i] = pre_num_change[i - coins[0]]

    for j in range(1, len(coins)):
        for k in range(1, change + 1):
            if k >= coins[j]:
                num_change[k] = (pre_num_change[k] + num_change[k - coins[j]])
            else:
                num_change[k] = pre_num_change[k]
        pre_num_change = num_change

    return num_change[-1]

print (num_change(30, [25, 10, 5, 1]))
