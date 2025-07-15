'''Addresses to Data

So how do we 'access' this memory from code?

Each piece of data within RAM has a memory address attached to it's value. It's like a real postal address to the location of a house.

This is very convenient for the computer, because it enables the processor to quickly locate and retrieve data.

The address of a piece of information is stored within a pointer. A pointer is simply a variable that stores a memory address. Every piece of data gets assigned a specific address, accessible by a pointer.

Quite a few programming languages, like python, make this very easy, due to built-in methods and simplification. This has it's benefits; we don't have to think about it on a functional level and focus more on efficiency.
'''


x = 42
y = x  # y points to the same memory address as x

print(f"Memory address of x: {id(x)}")
print(f"Memory address of y: {id(y)}")

y = 100
print(f"Memory address of y after change: {id(y)}")  # New memory address
print(f"Value of x: {x}")
print(f"Value of y: {y}")
