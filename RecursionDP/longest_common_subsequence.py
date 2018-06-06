
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
