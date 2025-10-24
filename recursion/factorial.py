"""Simple recursive factorial example.

Defines fact(n) which returns n! using recursion.
Includes a guard so the example runs only when executed directly.
"""

def fact(a):
    # Base case: 0! and 1! are defined as 1 to stop recursion.
    if (a == 0 or a == 1):
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return a * fact(a-1)

if __name__ == "__main__":
    # This block runs only when the file is executed directly (not when imported).
    # Print factorial of 5 (5! = 120).
    print(fact(5))