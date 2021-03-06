
import re


def valid_roman(s):
    match = re.search(
        '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', s)
    return True if match else False


print(valid_roman('XILI'))
print(valid_roman('XIX'))
print(valid_roman('XCD'))
print(valid_roman('XIXLI'))
