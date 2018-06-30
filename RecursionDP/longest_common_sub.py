
def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    index = L[m][n]
    lcs = [""] * (index)
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs[index-1] = s1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs)


print(longest_common_subsequence("AGGTAB", "GXTXAYB"))


def longest_common_substring(A, B):
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    max_length = 0
    max_length_last_index = None
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_length_last_index = i
    return A[max_length_last_index - max_length: max_length_last_index]


print(longest_common_substring("abcdaf", "zbcdf"))
