"""Finite exhaustive check for A351913(102), using SymPy arithmetic.

Run from this directory: python verify.py
Dependency used for the recorded run: sympy==1.14.0
Generated and executed by an AI assistant at Wang Lu's request.
This is a separate library-based implementation, not a human review.
"""

from datetime import datetime, timezone
from math import gcd, isqrt
import platform
from time import perf_counter
import sympy
from sympy import divisors, divisor_count


def verify(N=102):
    # tau(k)^3 <= (1536/35)*k and k <= d+N*d^2 imply
    # 35*d^2 <= 1536*N*d+1536. Compute the root using integers.
    B = 1536 * N
    D = (B + isqrt(B * B + 4 * 35 * 1536)) // 70
    assert 35 * D * D <= B * D + 1536
    assert 35 * (D + 1) ** 2 > B * (D + 1) + 1536

    checked = 0
    solutions = []
    for d in range(1, D + 1):
        for g_sym in divisors(d * d):
            g = int(g_sym)
            if gcd(N, d * d // g) != 1:
                continue
            checked += 1
            k = d + N * g
            if divisor_count(k) == d:
                # Check the original reduced numerator too.
                numerator = (k - d) // gcd(k - d, k * d)
                assert numerator == N
                solutions.append((k, d, g))
    return D, checked, sorted(solutions)


if __name__ == "__main__":
    print("UTC:", datetime.now(timezone.utc).isoformat())
    print("Python:", platform.python_version())
    print("SymPy:", sympy.__version__)
    start = perf_counter()
    D, checked, solutions = verify()
    print("Target numerator:", 102)
    print("Maximum d:", D)
    print("Admissible (d, g) candidates:", checked)
    print("Solutions (k, d, g):", solutions)
    print("Result:", min(k for k, _, _ in solutions) if solutions else -1)
    print("Elapsed seconds:", f"{perf_counter() - start:.6f}")
