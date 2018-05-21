from collections import Counter


def is_permutation_of_palindrome(phrase):
    # Given a string, write a function to check if it is a permutation of a palindrome.
    # Time O(N), where N is the length of the string.
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


def create_bit_vector(phrase):
    bit_vector = 0
    for c in phrase:
        x = ord(c) - 97
        bit_vector = toggle(bit_vector, x)
    return bit_vector


def toggle(bit_vector, x):
    if x < 0:
        return bit_vector
    mask = 1 << x
    return bit_vector ^ mask


def check_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


print(is_permutation_of_palindrome('tacocat'))


def can_string_be_a_palindrome(s):
    # Pythonic Solution
    # Time O(N), Space O(N), where N is the length of the string.
    return sum(v % 2 for v in Counter(s).values()) <= 1


print(can_string_be_a_palindrome('taocat'))
