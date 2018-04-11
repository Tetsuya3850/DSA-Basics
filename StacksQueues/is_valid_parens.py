
def is_valid_paren(s):
    lookup = { '(': ')', '[': ']', '{': '}' }
    stack = []
    for chr in s:
        if chr in lookup:
            stack.append(chr)
        else:
            if not stack or lookup[stack[-1]] != chr:
                return False
            else:
                stack.pop()
    return not stack
