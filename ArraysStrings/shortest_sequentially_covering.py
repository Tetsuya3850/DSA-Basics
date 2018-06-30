
def smallest_sequentially_covering(paragraph, keywords):
    # Time O(N), Space O(M), where N is the length of the paragraph and M is the length of keywords
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float("inf")] * len(keywords)
    shortest_dist = float('inf')
    result = (-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx-1] != float('inf'):
                distance_to_previous_keyword = (
                    i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = distance_to_previous_keyword + \
                    shortest_subarray_length[keyword_idx-1]
            latest_occurrence[keyword_idx] = i
            if keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_dist:
                shortest_dist = shortest_subarray_length[-1]
                result = (i-shortest_dist+1, i)
    return result
