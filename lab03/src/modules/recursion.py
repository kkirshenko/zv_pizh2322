def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Временная сложность: O(n).
# Глубина рекурсии: n — вызовы образуют цепочку длиной n.

def fibonacci_naive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# Временная сложность: экспоненциальная — O(φⁿ), где φ ≈ 1.618.
# Глубина рекурсии: n — максимальная цепочка вызовов достигает n уровней (например, fib(n) → fib(n−1) → …).

def pow_fast(a: float, n: int) -> float:
    if n < 0:
        return 1.0 / pow_fast(a, -n)
    if n == 0:
        return 1.0
    if n == 1:
        return a
    if n % 2 == 0:
        half = pow_fast(a, n // 2)
        return half * half
    else:
        half = pow_fast(a, (n - 1) // 2)
        return a * half * half

# Временная сложность: O(log n) — количество умножений логарифмическое.
# Глубина рекурсии: O(log n) — на каждом шаге показатель степени делится пополам.
