# A351913(102): a finite computational proof of a(102) = −1

**Status (5 October 2026):** an AI-assisted research note awaiting independent human verification. No OEIS entry modification for this result has been submitted. This publication does not imply OEIS approval or historical priority.

## Definition and exact candidate conditions

For a positive integer k, put d = τ(k), the number of its positive divisors. By [A352483](https://oeis.org/A352483), F(k) is the numerator of (k − d)/(kd) in lowest terms. [A351913](https://oeis.org/A351913) asks for the least k giving F(k) = N, or −1 if no such k exists.

For a solution with N > 0, let

$$g=\gcd(k-d,kd)=\gcd(k-d,d^2).$$

The equality follows from kd = d(k − d) + d². A solution thus satisfies k − d = Ng and g divides d². Furthermore,

$$g=\gcd(Ng,d^2)=g\gcd(N,d^2/g),$$

so gcd(N, d²/g) = 1. Conversely, if positive integers d and g satisfy

$$g\mid d^2,\qquad \gcd(N,d^2/g)=1,\qquad k=d+Ng,\qquad\tau(k)=d,$$

then gcd(k − d, kd) = gcd(Ng, d²) = g, and F(k) = N. These conditions are therefore **necessary and sufficient**, provided d is checked against the actual divisor count of k. Merely constructing k = d + Ng is insufficient.

In particular, every solution obeys

$$k\le d+Nd^2.$$

## A universal divisor-count bound

We prove

$$\boxed{\tau(k)^3\le\frac{1536}{35}k}.$$

For a prime factorization k = ∏ p^e, the divisor formula gives

$$\frac{\tau(k)^3}{k}=\prod_{p^e\parallel k}\frac{(e+1)^3}{p^e}.$$

For each prime p, define f_p(e) = (e + 1)³/p^e for integers e ≥ 0. Its consecutive ratio

$$\frac{f_p(e+1)}{f_p(e)}=\frac{1}{p}\left(\frac{e+2}{e+1}\right)^3$$

decreases with e. This identifies the maxima exactly:

| Prime | Maximizing exponent | Maximum |
| --- | --- | --- |
| 2 | 3 | 8 |
| 3 | 2 | 3 |
| 5 | 1 | 8/5 |
| 7 | 1 | 8/7 |
| p ≥ 11 | 0 | 1 |

For clarity, at p = 2 the ratios from e = 2 to 3 and from 3 to 4 are 32/27 > 1 and 125/128 < 1. At p = 3 the transition ratios are 9/8 > 1 and 64/81 < 1. For p = 5, 7 the first ratio 8/p exceeds 1 and the next 27/(8p) is below 1. For p ≥ 11 even the first ratio is below 1, as are all later ratios. Absent primes have exponent zero and contribute 1.

Multiplying the maxima gives 8 · 3 · (8/5) · (8/7) = 1536/35. Equality occurs at k = 2³ · 3² · 5 · 7 = 2520, where τ(k) = 48.

## Finite bound for d

Combining d³ ≤ (1536/35)k with k ≤ d + Nd² and dividing by d > 0 gives

$$35d^2\le1536Nd+1536.$$

For N = 102 this becomes

$$35d^2\le156672d+1536.$$

The quadratic has one negative root and one positive root. At d = 4476 the two sides are 701210160 and 701265408, respectively; at d = 4477 they are 701523515 and 701422080. Therefore its positive root lies strictly between 4476 and 4477, and every solution has

$$\boxed{1\le d\le4476}.$$

For completeness, this also implies k ≤ 4476 + 102 · 4476² = 2043531228, although our computation does not enumerate all those k.

## Exhaustive computation and conclusion

[verify.py](verify.py) loops over **every** integer d from 1 through 4476, enumerates **every** positive divisor g of d² using SymPy, retains exactly those with gcd(102, d²/g) = 1, and tests whether τ(d + 102g) = d using SymPy's `divisor_count`.

The [recorded output](run-output.txt), produced by an AI agent on 5 October 2026 with Python 3.12.14 and SymPy 1.14.0, reports:

```text
Target numerator: 102
Maximum d: 4476
Admissible (d, g) candidates: 29538
Solutions (k, d, g): []
Result: -1
```

The count refers to candidate **pairs**, not necessarily distinct k. Duplicate candidate k, if any, would not affect completeness. If a solution existed, its actual d and g would satisfy the necessary conditions above, fall within this finite loop, and pass the divisor-count test. The run finds none. Thus the argument together with this exact computation gives

$$\boxed{A351913(102)=-1}.$$

This is a computational proof, not a purely symbolic exclusion of all candidates. Its arithmetic implementation and its mathematical completeness argument are both available for independent verification. It does not rely on a previous large forward search.

## General finite decision procedure

For any fixed positive integer N, the same reasoning bounds d by

$$D(N)=\left\lfloor\frac{1536N+\sqrt{(1536N)^2+4\cdot35\cdot1536}}{70}\right\rfloor.$$

The program computes this bound using integer square root and asserts that D satisfies the inequality while D + 1 does not. Enumerating the necessary and sufficient candidate conditions for 1 ≤ d ≤ D(N) gives a finite decision procedure. If solutions exist, take the least k **over all solutions**; the d, g loop is not ordered by increasing k. This observation does not establish historical novelty or settle every unknown entry in the OEIS table: only N = 102 is reported here.

## Provenance and references

This reduction and calculation were developed in AI-assisted discussions involving Wang Lu, Claude and GPT. Wang Lu is studying the proof; the actual program execution was performed by an AI agent. No independent human certification is claimed. The library-based implementation follows a suggestion to use established arithmetic libraries, but no mathematical endorsement by the person making that suggestion is implied.

- [OEIS A351913](https://oeis.org/A351913): problem and conjecture (conjecture credited to Paolo Xausa).
- [OEIS A352483](https://oeis.org/A352483): numerator definition.
- [SymPy documentation](https://docs.sympy.org/latest/modules/ntheory.html): `divisors` and `divisor_count`.
