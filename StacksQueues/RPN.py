
def RPN(expression):
    # Time O(N), where N is the length of the expression string.
    intermediate_results = []
    DELEIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in expression.split(DELEIMITER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]


print(RPN('3,4,+,2,*,1,+'))
