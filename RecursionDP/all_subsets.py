def all_subsets(A):
    # Time complexity O(N2^N). Space complexity O(N2^N).
    results = []
    results.append([])
    for item in A:
        new_results = []
        for result in results:
            new_results.append(result + [item])
        results.extend(new_results)
    return results


print(all_subsets(['A', 'B', 'C']))


def all_subsets_recursive(A):
    # Time complexity O(N2^N). Space complexity O(N).
    def directed_subset(to_be_selected, selected_so_far):
        if to_be_selected == len(A):
            results.append(selected_so_far)
            return
        directed_subset(to_be_selected + 1, selected_so_far)
        directed_subset(to_be_selected + 1,
                        selected_so_far + [A[to_be_selected]])

    results = []
    directed_subset(0, [])
    return results


print(all_subsets_recursive(['A', 'B', 'C']))


def all_subsets_bit(A):
    # Time complexity O(2^N). Space complexity O(N).
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


print(all_subsets_bit(['A', 'B', 'C']))


def all_subsets_dup(S):
    res = [[]]
    S.sort()
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
            res.append(res[j] + [S[i]])
    return res


print(all_subsets_dup(['A', 'B', 'B']))
