
def floating_to_binary(n):
    if n >= 1 or n <= 0:
        return False
    result = ['.']
    while n > 0:
        if len(result) >= 32:
            return False
        n *= 2
        if n >= 1:
            result.append('1')
            n -= 1
        else:
            result.append('0')
    return ''.join(result)


print(floating_to_binary(0.890625))
