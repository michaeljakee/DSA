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


data = [i for i in range(1, 10**6)]  # A list of 1 million integers

print(data[100]) # Direct access to the 101st element

def load_data():
    data_in_memory = [i for i in range(1, 10**6)] # Large data loaded into RAM
    return data_in_memory

large_data = load_data()
print("First 5 elements of large data:", large_data[:5]) # Working with data in RAM

data = [i for i in range(1, 10**5)]

print(data[100])

def load_data():
    data_in_memory = [i for i in range (1, 10**5)]
    return data_in_memory
large_data = load_data()
print("last 5 elements of large data:", large_data[:5])

