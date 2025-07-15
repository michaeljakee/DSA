""" DSA has two terms, Data Structures and Algorithms. Let's break each term down:

Data Structures are just a medium in which we store/organise data on a computer. If you have used python, you would have seen several built-in data types such as lists, strings, dictionaries, etc.

Algorithms are step-by-step procedures that aim to solve a problem. For example, solving a Rubik's Cube would involve a series of algorithms.

Beginner programmers often focus primarily on finding solutions to problems, while more experienced developers understand that the true challenge lies in optimizing those solutions for efficiency.
As an expert, when we look at programming problems, we aim to use a combination of data structures and algorithms to find the quickest solution, while using the least amount of computer space.

This is when we can leverage our understanding of DSA!

Using DSA to solve computing problems is quite similar to building a house. To ensure the house is as quality as possible, and build the house as quickly as possible, we would like to use the highest quality tools (data structures), and a blueprint (algorithms) which builds the house as quickly as possible."""

# A list is a data structure to store multiple values
numbers = [4, 3, 5, 1, 2]

# Algorithms: Example of a sorting algorithm (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Using the data structure and algorithm
print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted list:", numbers)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print("original list:", numbers)
bubble_sort(numbers)
print("sorted list:", numbers)
