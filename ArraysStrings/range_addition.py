
def range_addition(length, updates):
    # Assume you have an array of length n initialized with all 0's and are given k update operations.
    # Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments
    # each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
    # Return the modified array after all k operations were executed.
    # Time O(L + U), Space O(1), where L is the length and U is the num of updates.
    result = [0] * length
    for update in updates:
        result[update[0]] += update[2]
        if update[1] < length - 1:
            result[update[1] + 1] += -update[2]
    for i in range(1, length):
        result[i] += result[i-1]
    return result


print(range_addition(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
