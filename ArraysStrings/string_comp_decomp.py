
def string_compression(s):
    # Time complexity O(N), Space complexity O(1), where N is the length of the string.
    result = []
    count_consecutive = 0
    for i in range(len(s)):
        count_consecutive += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            if count_consecutive > 1:
                result.append(str(count_consecutive))
                result.append('[')
                result.append(s[i])
                result.append(']')
            else:
                result.append(s[i])
            count_consecutive = 0
    return ''.join(result)


print(string_compression('aaabbccd'))
print(string_compression('abcd'))


def string_decompression(s):
    class Result:
        def __init__(self, decoded_str, end_i):
            self.decoded_str = decoded_str
            self.end_i = end_i

    def helper(s, i):
        duplication = 0
        while s[i].isnumeric():
            duplication *= 10
            duplication += int(s[i])
            i += 1
        result = []
        if duplication == 0:
            while i < len(s) and not s[i].isnumeric():
                result.append(s[i])
                i += 1
            return Result("".join(result), i)
        else:
            i += 1
            while s[i] != ']':
                if s[i].isnumeric():
                    part_result = helper(s, i)
                    result.append(part_result.decoded_str)
                    i = part_result.end_i
                else:
                    result.append(s[i])
                    i += 1
            return Result(duplication * "".join(result), i + 1)

    decoded = []
    i = 0
    while i < len(s):
        part_result = helper(s, i)
        decoded.append(part_result.decoded_str)
        i = part_result.end_i
    return "".join(decoded)


print(string_decompression('3[abc]4[ab]c'))
print(string_decompression('10[a]'))
print(string_decompression('2[3[a]b]'))
