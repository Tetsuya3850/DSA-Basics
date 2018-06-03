

def levenshtein_dist(A, B):
    def compute_prefix_dist(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        elif B_idx < 0:
            return A_idx + 1
        if dist_prefix[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                dist_prefix[A_idx][B_idx] = compute_prefix_dist(
                    A_idx-1, B_idx-1)
            else:
                substitute_last = compute_prefix_dist(A_idx-1, B_idx-1)
                add_last = compute_prefix_dist(A_idx-1, B_idx)
                delete_last = compute_prefix_dist(A_idx, B_idx-1)
                dist_prefix[A_idx][B_idx] = 1 + \
                    min(substitute_last, add_last, delete_last)
        return dist_prefix[A_idx][B_idx]

    dist_prefix = [[-1] * len(B) for _ in A]
    return compute_prefix_dist(len(A)-1, len(B)-1)


print(levenshtein_dist("Carthorse", "Orchestra"))
