
def well_formed(s):
    # A program that tests if a string made up of the charcters (), [], {} is well-formed.
    # Time O(N), Space O(N), where N is the length of the string.
    stack, lookup = [], {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in lookup:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if lookup[top] != c:
                    return False
    return not stack


print(well_formed('([]){()}'))
print(well_formed('([])()}'))
