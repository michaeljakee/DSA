'''The ability to efficiently analyze and manipulate vast amounts of data is a critical skill in quantitative finance.

Researchers, quantitative analysts, and software engineers often deal with terabytes of data generated daily by financial markets, trading systems, and other sources.

Efficient programming techniques are a necessity. Even seemingly small inefficiencies in code can lead to massive computational overhead when working at scale.

For example, consider the implications of algorithm complexity:

Linear Complexity (O(n)): A dataset with 1 million data points will require 1 million iterations.
Quadratic Complexity (O(n2)): A double-nested loop would scale this to 1 trillion iterations (1 million * 1 million).
Exponential Complexity (O(2n)): Even with smaller datasets, exponential growth becomes computationally prohibitive.
Scaling inefficiencies not only slow down processes but can also lead to increased costs in cloud computing, higher energy consumption, and delayed decision making.

As such, it is imperative, as a quant, you choose the right data structures and refine your algorithms to be as efficient as possible.'''

# Example of inefficiency with a nested loop (O(n^2) complexity)
def inefficient_algorithm(data):
    n = len(data)
    for i in range(n):
        for j in range(n):
            # Simulate some operation on data points
            pass

# Example of efficient loop (O(n) complexity)
def efficient_algorithm(data):
    for i in range(len(data)):
        # Simulate some operation on data points
        pass

# Simulating a large dataset (1 million data points)
data = [i for i in range(1, 10**6)]

# Efficient approach (O(n))
print("Running efficient algorithm...")
efficient_algorithm(data)

# Inefficient approach (O(n^2))
"""print("Running inefficient algorithm...")
inefficient_algorithm(data)"""
