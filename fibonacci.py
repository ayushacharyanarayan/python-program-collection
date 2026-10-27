"""Fibonacci program: series generation and recursion."""


def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Position cannot be negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    try:
        terms = int(input("How many terms? "))
        if terms <= 0:
            print("Please enter a number greater than 0.")
        else:
            print("Series:", fibonacci_series(terms))
            print(f"Term {terms} (recursion):", fibonacci_recursive(terms - 1))
    except ValueError as error:
        print("Error:", error)
