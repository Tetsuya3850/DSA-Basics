def string_compression(s):
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

print (string_compression('aaabbccd'))
print (string_compression('abcd'))

def string_decompression(s):
    def string_decompression_helper(s):
        nonlocal i
        result = []
        while i < len(s):
            if s[i].islower():
                single_text = []
                while i < len(s) and s[i].islower():
                    single_text.append(s[i])
                    i += 1
                result.append(''.join(single_text))
            else:
                sub_times = 0
                while s[i].isdigit():
                    sub_times = sub_times * 10 + int(s[i])
                    i += 1
                i += 1
                sub_text = []
                while i < len(s) and s[i] != ']':
                    if s[i].islower():
                        sub_text.append(s[i])
                    else:
                        recur_text = string_decompression_helper(s)
                        sub_text.append(recur_text)
                    i += 1
                for _ in range(sub_times):
                    result.append(''.join(sub_text))
            i += 1
        return ''.join(result)

    i = 0
    return string_decompression_helper(s)

print (string_decompression('3[abc]4[ab]c'))
print (string_decompression('10[a]'))
print (string_decompression('2[3[a]b]'))
