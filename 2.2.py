'''Representing Data with Bytes

In computers, all of the data your store within your programs are represented in bytes. More complex data types are built using combinations of bytes.

The specific data type (i.e. integer, string, etc) defines how multiple bytes are grouped together to represent more complex information.

For example, if we wanted to store the string "hello" from memory, we would do the following:

1. Convert each character into it's corresponding ASCII value:

'H' - 01001000
'e' - 01100101
'l' - 01101100
'l' - 01101100
'o' - 01101111
All of these binary representations are stored as bytes in a 'clump' within memory.

To summarise, RAM stores data in bytes, and complex data types are constructed by combining multiple bytes. Every program you run and every file you open relies on this byte-based system.

You won't need to know EXACTLY how RAM works to excel in DSA; The foundational knowledge we have provided is sufficient to understand efficient programming techniques.
'''


text = "Hello"

byte_representation = [format(ord(char), '08b') for char in text]

for char, byte in zip(text, byte_representation):
    print(f"Character '{char}' -> ASCII: {ord(char)} -> Byte: {byte}")

byte_array = bytearray(text, 'utf-8')
print("Byte array representation:", byte_array)
