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


# O(1) Constant Time: Accessing an element in a list by index
def get_first_item(lst):
    return lst[0]

# O(n) Linear Time: Iterating over the list
def print_items(lst):
    for item in lst:
        print(item)

# O(n^2) Quadratic Time: Comparing each element with every other element
def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Simulating different input sizes
small_list = [1, 2, 3, 4]
large_list = [i for i in range(1, 10**4)]  # 10000 elements

# O(1) Example
print("O(1) Example:", get_first_item(small_list))

# O(n) Example
"""print("O(n) Example:")
print_items(small_list)"""

# O(n^2) Example (Inefficient algorithm)
"""print("O(n^2) Example:")
print(has_duplicate(large_list))"""
