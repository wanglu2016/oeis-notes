"""Check A204983 formula against direct least-pair enumeration (n <= 300).

AI-assisted code; recorded runs were executed by an AI agent.
This finite check is not the general mathematical proof.
"""

from datetime import datetime, timezone
import json
import platform


def formula(n):
    odd, exponent = n, 0
    while odd % 2 == 0:
        odd //= 2
        exponent += 1
    r = 1
    if odd > 1:
        residue = 2 % odd
        while residue != 1:
            residue = 2 * residue % odd
            r += 1
    return (1 << exponent) * ((1 << r) - 1)


def least_pair(n):
    k = 2
    while True:
        for j in range(1, k):
            difference = (1 << (k - 1)) - (1 << (j - 1))
            if difference % n == 0:
                return difference
        k += 1


if __name__ == "__main__":
    mismatches = [n for n in range(1, 301) if formula(n) != least_pair(n)]
    print("UTC:", datetime.now(timezone.utc).isoformat())
    print("Python:", platform.python_version())
    print(json.dumps({"checked_n": 300, "least_pair_mismatches": mismatches,
                      "a_20": formula(20)}, indent=2))
    if mismatches:
        raise SystemExit(1)
