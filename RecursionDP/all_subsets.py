# Write a method to return all subsets of a set.

# Time complexity O(N2^N). Space complexity O(N2^N).
def all_subsets(A):
    results = []
    results.append([])
    for item in A:
        new_results = []
        for result in results:
            new_results.append(result + [item])
        results.extend(new_results)
    return results

print (all_subsets(['A', 'B', 'C']))


# Time complexity O(N2^N). Space complexity O(N2^N).
def all_subsets_recursive(A):
    def directed_subset(to_be_selected, selected_so_far):
        if to_be_selected == len(A):
            results.append(selected_so_far)
            return
        directed_subset(to_be_selected + 1, selected_so_far)
        directed_subset(to_be_selected + 1, selected_so_far + [A[to_be_selected]])

    results = []
    directed_subset(0, [])
    return results

print (all_subsets_recursive(['A', 'B', 'C']))


# Time complexity O(N2^N). Space complexity O(N2^N).
def all_subsets_bit(A):
    def convert_int_to_set(i, A):
        subset = []
        idx = 0
        while i:
            if i & 1 == 1:
                subset.append(A[idx])
            idx += 1
            i >>= 1
        return subset

    results = []
    max_combination = 1 << len(A)
    for i in range(max_combination):
        subset = convert_int_to_set(i, A)
        results.append(subset)
    return results

print (all_subsets_bit(['A', 'B', 'C']))
