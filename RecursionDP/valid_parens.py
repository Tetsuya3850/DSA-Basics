# Implement an algorithm to print all valid conbinations of pairs of parentheses.

def valid_parens(n):
    def parens_helper(partial_result, l, r):
        if l == 0 and r == 0:
            print (partial_result)
            return
        if l > 0:
            parens_helper(partial_result + '(', l-1, r)
        if l < r:
            parens_helper(partial_result + ')', l, r-1)

    parens_helper('', n, n)

valid_parens(3)
