'''Lesson 2.1: Understanding Binary

Storing data in RAM, and in computers in general, everything is represented in binary code. Binary is the language of computers (and the matrix), where all data and information is represented with 1s and 0s.

Binary is a base-2 number system. Our normal decimal system is base 10. We count binary simliar to decimal, except we just stop at 1 instead of 9. Further, similar to numbers, we count from left to right.

Heres how decimal and binary relate:

Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...
Binary: 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010...
Each binary digit represents an increasing power of 2, just as each decimal digit represents an increasing power of 10.

E.g. The binary number 101 is equal to 1 * 23 + 0 + 1 * 21 = 5.

But how do we store characters? Well, we can use an encoding system like ASCII! This is a table that maps characters to numbers in binary.
'''


binary_number = '101'
decimal_value = int(binary_number, 2)  # Convert binary string to decimal
print(f"Binary {binary_number} is equal to Decimal {decimal_value}")

decimal_number = 5
binary_representation = bin(decimal_number)[2:]  # Remove the '0b' prefix
print(f"Decimal {decimal_number} is equal to Binary {binary_representation}")

char = 'A'
ascii_value = ord(char)  # Get ASCII value of character
binary_char = bin(ascii_value)[2:]  # Convert ASCII value to binary
print(f"Character {char} has ASCII value {ascii_value} and binary {binary_char}")
