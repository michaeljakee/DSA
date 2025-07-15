'''Different Notations of Time Complexity

We have discussed Big O notation to introduce time complexities of algorithms, however there are multiple different ways we can analyse time complexity.

Formally, Big O Notation is described as the upper bound or the worst-case scenario of an algorithm.

But there are also ways to measure the average-case scenario (Omega notation) and the best-case scenario (Theta notation).

But what is worst-case, average-case, and best-case scenario?

The best-case scenario is the function which performs the minimum number of steps on input data of n elements.

For example, if you're looking for the number 1 of an array, and there is a 1 at the start of the array, the best case is constant time O(1).

The Average-case scenario is the function which performs the average number of steps on input data, and the worst-case scenario is the function which performs the most number of steps on input data.
'''

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
