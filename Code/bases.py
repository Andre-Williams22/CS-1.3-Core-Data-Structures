#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    decoded_digits = 0
    for i, value in enumerate(digits[::-1]):
        decoded_digits += int(value, base) * (base**i)
    return decoded_digits 
    # digits_string = digits.lower().split('.')
    # exp = 0

    # try:
    #     exp = 0 - len(digits_string[1])
    # except:
    #     'No point'
    # decode = 0
    # for item in digits_string[::-1]:
    #     decimal = 0
    #     for digit in part[::-1]:
    #         decimal += (string.digits + string.ascii_lowercase).index(digit) * base**expexp +=1
    #     decode += decimal
    # return decode 

    '''
    reusable_nums = string.digits + string.ascii_lowercase

    toNum = 0
    power = 0
    for digit in digits:
        final = 10 * final + reusable_nums[digit]
        while final > 0:
            toNum += base1 ** power * (base1 % base2)
            final //= base
            power += 1
        return toNum  '''


    # ...
    # TODO: Decode digits from hexadecimal (base 16)


    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...
def digits_to_char(remainder=int) -> str:
    '''Converts a digit to a character value. '''
    return string.printable[remainder]

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
    # toNum = 0
    # power = 0
    # while digits > 0:
    #     toNum += base1 ** power * (base1 % base2)
    #     digits //= base2
    #     power += 1
    # return toNum

    encoded_numbers = ''
    while number > 0:
        number, rem = divmod(number, base)
        encoded_numbers += digits_to_char(rem)
    return encoded_numbers[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
        # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    return encode(decode(digits, base1), base2)

    # reusable = string.digits + string.ascii_lowercase
    # #reusable = dict()
    # toNum = 0
    # power = 0
    # final = ""
    # for digit in digits:
    #     final = 10 * final + reusable[digit]
    #     while final > 0:
    #         toNum += base1 ** power * (base1 % base2)
    #         final //= base
    #         power += 1
    #     return toNum

 
  


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
