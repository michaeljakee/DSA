'''Now try this challenge:

Given an integer n, convert it to its binary representation as a string. Do not use built-in functions or libraries to perform the conversion.

You need to implement a function that converts the given integer to a binary string. Ensure that the total number of bits in the result is a multiple of 8.

The input is in range 0 < n < 216 - 1

For example, integer_to_binary(5) returns "00000101", and integer_to_binary(500) returns "0000000111110100".
'''


def integer_to_binary(n):
    if n < 0 or n >= 65536:
        raise ValueError("Input must be in the range 0 < n < 216 - 1")

    binary_string = ""
    while n > 0:
        binary_string = str(n % 2) + binary_string
        n //= 2

    # Ensure the length is a multiple of 8
    while len(binary_string) % 8 != 0:
        binary_string = "0" + binary_string

    return binary_string 



def integer_to_binary(n: int) -> str:
    pass    
    