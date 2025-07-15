# DSA
data structure and algorithm

[1.1]
""" DSA has two terms, Data Structures and Algorithms. Let's break each term down:

Data Structures are just a medium in which we store/organise data on a computer. If you have used python, you would have seen several built-in data types such as lists, strings, dictionaries, etc.

Algorithms are step-by-step procedures that aim to solve a problem. For example, solving a Rubik's Cube would involve a series of algorithms.

Beginner programmers often focus primarily on finding solutions to problems, while more experienced developers understand that the true challenge lies in optimizing those solutions for efficiency.
As an expert, when we look at programming problems, we aim to use a combination of data structures and algorithms to find the quickest solution, while using the least amount of computer space.

This is when we can leverage our understanding of DSA!

Using DSA to solve computing problems is quite similar to building a house. To ensure the house is as quality as possible, and build the house as quickly as possible, we would like to use the highest quality tools (data structures), and a blueprint (algorithms) which builds the house as quickly as possible."""

[1.2]
'''The ability to efficiently analyze and manipulate vast amounts of data is a critical skill in quantitative finance.

Researchers, quantitative analysts, and software engineers often deal with terabytes of data generated daily by financial markets, trading systems, and other sources.

Efficient programming techniques are a necessity. Even seemingly small inefficiencies in code can lead to massive computational overhead when working at scale.

For example, consider the implications of algorithm complexity:

Linear Complexity (O(n)): A dataset with 1 million data points will require 1 million iterations.
Quadratic Complexity (O(n2)): A double-nested loop would scale this to 1 trillion iterations (1 million * 1 million).
Exponential Complexity (O(2n)): Even with smaller datasets, exponential growth becomes computationally prohibitive.
Scaling inefficiencies not only slow down processes but can also lead to increased costs in cloud computing, higher energy consumption, and delayed decision making.

As such, it is imperative, as a quant, you choose the right data structures and refine your algorithms to be as efficient as possible.'''

[1.3]
'''Time Complexity is measuring how long it takes an algorithm to perform certain tasks as the input size increases.

However, time complexity isn't measured in seconds. It is measured in 'rates' or change in time.

For example, view the terminal. We have an (inefficient) algorithm that compares each string to another string, and prints true if there is a copy.

Although the algorithm runs pretty quickly with small amounts of data, it slows down dramatically with large amounts of data (as explained in 1.2).

This algorithm would be explained as O(n2) in time complexity. This is because it iterates over the input (n), n times.


The following is a list of the most common time complexities:

O(1) Constant Time: Super fast! Regardless of input size, it takes basically the same time. For example, getting the first item in a list.
O(logn) Logarithmic Time: Very fast! execution time increases logarithmically with input. For example, guessing a number by splitting in half each time.
O(n) Linear Time: Pretty fast! time of execution increases linearly with input size. For example, printing every item in a list.
O(n2) Quadratic Time: Not very fast. Time of execution increases quadratically with input size. For example, our algorithm we just discussed.
O(2n) Exponential Time: Very slow. Time of execution increases exponentially with input size. For example, combinatoric calculations.'''

[1.4]
'''Different Notations of Time Complexity

We have discussed Big O notation to introduce time complexities of algorithms, however there are multiple different ways we can analyse time complexity.

Formally, Big O Notation is described as the upper bound or the worst-case scenario of an algorithm.

But there are also ways to measure the average-case scenario (Omega notation) and the best-case scenario (Theta notation).

But what is worst-case, average-case, and best-case scenario?

The best-case scenario is the function which performs the minimum number of steps on input data of n elements.

For example, if you're looking for the number 1 of an array, and there is a 1 at the start of the array, the best case is constant time O(1).

The Average-case scenario is the function which performs the average number of steps on input data, and the worst-case scenario is the function which performs the most number of steps on input data.
'''

[2.0]
'''Lesson 2.0: Understanding RAM

Random Access Memory (RAM, or just memory) is a computer's 'short-term' memory.

Memory is where the data is stored that your computer processor needs to run applications and open your files.

This includes everything from system processes to the data used by the programs you run, as well as the data in your code while it is executing.

When you open a program or a file, the operating system loads that data into RAM from the hard drive or SSD. This is because RAM is much quicker to access than storage.

RAM is volatile, meaning that when you turn the power off, the data stored within it is lost.

Modern computers commonly come with 8 gigabytes or 16 gigabytes of RAM, but what do these numbers actually mean?

'giga' - This is just a scalar multiplier 109, or 1 billion.
'bytes' - A set of 8 bits (i.e. a position that can store a 1 or a 0).
But how does RAM, bytes, and data structures all work harmoniously to store data, and how can we use this to run efficient programs?'''

[2.1]
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
[2.2]
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
[2.3]
'''Addresses to Data

So how do we 'access' this memory from code?

Each piece of data within RAM has a memory address attached to it's value. It's like a real postal address to the location of a house.

This is very convenient for the computer, because it enables the processor to quickly locate and retrieve data.

The address of a piece of information is stored within a pointer. A pointer is simply a variable that stores a memory address. Every piece of data gets assigned a specific address, accessible by a pointer.

Quite a few programming languages, like python, make this very easy, due to built-in methods and simplification. This has it's benefits; we don't have to think about it on a functional level and focus more on efficiency.
'''
[2.4]
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
    
