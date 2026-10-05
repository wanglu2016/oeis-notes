# OEIS research notes

AI-assisted mathematical explorations organized by **Wang Lu (王路)**.
These notes publish arguments and reproducible computations for inspection.
They do not claim historical priority or independent human verification.

[中文说明](README-zh.md)

## Results and review status

Status snapshot: **5 October 2026**. Follow the linked OEIS history for later changes.

| Problem | Material | Status |
| --- | --- | --- |
| [A204983](https://oeis.org/A204983) | [Elementary proof](A204983/proof.md), [verification program](A204983/verify.py), [recorded output](A204983/run-output.txt) | Submitted to OEIS on 4 October 2026; latest observed draft revision 31 is **proposed**, not approved. |
| [A351913(102)](https://oeis.org/A351913) | [Finite computational proof of a(102) = -1](A351913-102/proof.md), [SymPy program](A351913-102/verify.py), [recorded output](A351913-102/run-output.txt) | Public research note awaiting independent human verification; no OEIS entry modification has been submitted for this result. |

A204983 concerns the least pair of distinct powers of 2 with a difference divisible by n. The formula listed by Andrew T. Porter in 2022 follows from factoring that difference into a power of 2 and an odd factor.

For A351913(102), the proposed proof converts an unbounded search over k into a finite, exhaustive search over d = tau(k) and divisors g of d². The rigorous bound is d ≤ 4476. The recorded run checks **29,538 admissible (d, g) pairs** and finds **no solutions**. This is a computer-assisted proof whose conclusion depends on both the mathematical reduction and the exact arithmetic computation.

## Reproduce

Python 3.12.14 and SymPy 1.14.0 were used for the recorded SymPy run.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python A204983/verify.py
python A351913-102/verify.py
```

The first program uses only the Python standard library. The second uses SymPy's `divisors` and `divisor_count` rather than implementing its own factorization. Timestamps and elapsed times vary between runs; the mathematical outputs should agree. The A204983 calculation is a finite consistency check; its general proof does not depend on that calculation.

## Provenance and AI assistance

Wang Lu initiated the exploration, supplied the English proof text used for the A204983 submission after AI-assisted discussion, authorized publication, and is studying the arguments. Claude and GPT participated in the mathematical exploration and checking. GPT prepared this repository presentation and the verification code. **An AI agent, rather than Wang Lu personally, executed the recorded computations.** Cross-checking between AI systems is not independent human review.

The A204983 formula is credited to Andrew T. Porter (20 December 2022) in OEIS; the sequence is credited there to Clark Kimberling. The A351913 problem and conjecture are taken from OEIS, with the conjecture credited there to Paolo Xausa. No claim that these arguments are the first proofs in the literature is made. No endorsement by OEIS, its editors, or the sequence authors is implied.

## Sources and discussion

- [A204983 draft](https://oeis.org/draft/A204983) and [submission revision 29](https://oeis.org/history/view?seq=A204983&v=29)
- [A351913](https://oeis.org/A351913) and [A352483](https://oeis.org/A352483)
- [SymPy number theory documentation](https://docs.sympy.org/latest/modules/ntheory.html)

Corrections and independently reproduced results are welcome through GitHub Issues. Please identify the mathematical step or program version being checked. The general finite-search reduction is included, but this repository does **not** claim to have settled all unknown entries up to 10000.
