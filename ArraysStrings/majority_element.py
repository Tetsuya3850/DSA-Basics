
def majority_element(A):
    # Time O(N), Space O(1), where N is the length of the array.
    candidate_majority_element = find_candidate_majority_element(A)
    return candidate_majority_element if validate_candidate_element(A, candidate_majority_element) else False


def find_candidate_majority_element(A):
    # Time O(N), Space O(1), where N is the length of the array.
    majority = 0
    count = 0
    for integer in A:
        if count == 0:
            majority = integer
        if integer == majority:
            count += 1
        else:
            count -= 1
    return majority


def validate_candidate_element(A, majority):
    # Time O(N), Space O(1), where N is the length of the array.
    count = 0
    for integer in A:
        if integer == majority:
            count += 1
    return count > len(A) / 2


print(majority_element([5, 5, 5, 9, 9, 9, 1, 5, 5]))
