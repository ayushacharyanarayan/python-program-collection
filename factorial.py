"""Factorial program: iterative and recursive methods."""


def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} (loop): {factorial_iterative(num)}")
        print(f"Factorial of {num} (recursion): {factorial_recursive(num)}")
    except ValueError as error:
        print("Error:", error)
