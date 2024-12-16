#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Generate the Fibonacci sequence up to the specified length
    fibonacci_sequence = []
    for _ in range(length):
        fibonacci_sequence.append(a)  # Append the current Fibonacci number
        a, b = b, a + b  # Update a and b to the next two Fibonacci numbers
    
    # Print the Fibonacci sequence
    print(fibonacci_sequence)

   