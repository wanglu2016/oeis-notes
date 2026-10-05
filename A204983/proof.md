# A204983: proof of the listed formula

**Status (5 October 2026):** submitted to OEIS; the latest observed draft revision 31 remains proposed. This note does not claim editorial approval or historical priority.

The formula is credited in [OEIS A204983](https://oeis.org/A204983) to Andrew T. Porter, 20 December 2022. The following argument was explored with Claude and GPT. Wang Lu supplied the English proof text used in the submission; this repository version presents the same argument with mathematical typesetting.

Write

$$n=2^a m,\qquad m\text{ odd},$$

and let r be the smallest positive integer for which m divides 2^r − 1. Such an integer exists because 2 is invertible modulo the odd integer m: among its powers two residues coincide, and cancellation produces a positive power congruent to 1. For m = 1, use r = 1.

For integers 1 ≤ j < k,

$$2^{k-1}-2^{j-1}=2^{j-1}(2^{k-j}-1).$$

The second factor is odd. Since 2^a and m are coprime, n divides this difference exactly when

$$j-1\ge a\quad\text{and}\quad m\mid 2^{k-j}-1.$$

The second condition implies k − j ≥ r by the minimality of r. Consequently every valid pair satisfies

$$k=(j-1)+(k-j)+1\ge a+r+1.$$

Taking j = a + 1 and k = a + r + 1 satisfies both conditions and attains the bound. At this k, increasing j violates the second condition and decreasing j violates the first, so the pair is unique. Therefore

$$\boxed{a(n)=2^a(2^r-1)}.$$

Here a = A007814(n) and r = A007733(n), including its convention for odd part 1. This proves the formula for the ordering used by the OEIS PARI program (increasing k, then increasing j).

If the definition is instead interpreted as minimizing the numerical difference, the same result follows: every valid difference is 2^p(2^q − 1), where p ≥ a and q ≥ r. This expression is strictly increasing in each variable, and p = a, q = r is valid.

For example, n = 20 = 2² · 5. The first positive q with 5 dividing 2^q − 1 is 4, giving a(20) = 4 · 15 = 60.

## Computational consistency check

[verify.py](verify.py) compares the formula with direct enumeration in the original pair order for 1 ≤ n ≤ 300. [run-output.txt](run-output.txt) records an actual AI-agent execution. A finite check supports the implementation but is not the proof of the general formula.

## Submission record

The proof was added in [revision 28](https://oeis.org/history/view?seq=A204983&v=28) and submitted for review in [revision 29](https://oeis.org/history/view?seq=A204983&v=29), 4 October 2026 at 19:51:35 EDT. [The draft](https://oeis.org/draft/A204983) contains the current review history. The original formula attribution is retained.
