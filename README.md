# Explicit bounds for Erdős’s minimum-overlap problem

**Cristian Budala — University of Bucharest**

This repository contains a paper, complete coefficient data and exact-arithmetic checkers for two bounds on the ordered minimum-overlap problem:

```text
L = 3945957506942881/10368080969891328
  ≈ 0.38058706508965855
U = 1247990868533174455263346437/3276800000000000000000000000
  ≈ 0.38085658829747756
```

For every positive integer N, every balanced partition of {1,...,2N} has an ordered signed difference occurring at least L*N times. The paper also constructs balanced partitions with normalized maximum at most U plus an explicit error tending to zero. Thus L <= liminf M(N)/N <= limsup M(N)/N <= U, without requiring a limit-existence theorem.

## Read and reproduce

- [Paper (PDF)](paper/erdos36_bounds.pdf)
- [Paper source](paper/erdos36_bounds.tex) and [references](paper/references_main.tex)
- [Human, method and software credits (PDF)](paper/research_credits.pdf) and [text](paper/research_credits.md)
- [Verification guide](verification/README.md)
- [Factual source-reference register](paper/source_references.json)

From the repository root, using ordinary assertion-enabled Python3 on a POSIX system:

```bash
python3 -I -S -B verification/verify_erdos36_l60.py
python3 -I -S -B verification/verify_erdos36_u54.py
python3 -I -S -B verification/verify_arena_upload.py arena
```

No third-party packages, optimizer, network or private research tree are needed for these checks. Do not use `-O` or `-OO`. Both bound checkers embed their full data. The SHA-256 inventory covers the published files other than the inventory itself.

## Arena representation

[The Arena upload](arena/solution.json) is a separate 2048-cell dyadic profile. Its exact decimal JSON and binary64 values coincide and have exact mass one. The supplied certificate checks all 4097 signed events and the full real-lag maximum by affine interpolation.

The downloaded official verifier evaluated it locally at **0.38085658829748237**, without rescaling. Its exact maximum is about 4.81e-15 above the paper’s U, and its maximizing shifts are +/-311/1024 rather than the original profile’s +/-295/1024. These constructions and their scores are not silently identified. The local verifier result is not a claim of server acceptance or rank.

## Arena submission

The dyadic construction was submitted to EinsteinArena as **solution 2623** on 2026-10-15. The server returned `pending`; evaluation is asynchronous. The local score above is not being presented as an evaluated server score or a rank. [Current solution status](https://einsteinarena.com/api/solutions/2623).

Earlier Arena discussions by **TuringAgent9811 (thread 65)**, **AlanTuringCodex_floor9 (thread 67)** and **DarwinAgent8427 (thread 86)** explain the exact-sum dyadic representation and rescaling pitfall. They are credited for that context. Our fixed 40-bit export uses standard largest-remainder rounding and claims no new rounding method. These public handles are not treated as verified individual human identities.

## Status, attribution and AI assistance

This is a computer-assisted bounds paper, not a complete solution of Problem36 or a claim of independent human peer review or unconditional public-record priority. The lower certificate builds on White, Price, Raval, Deng and Machillari Dowguñiec. The upper construction refines a balanced repair of the rounded public MILO data; MILO’s authors are credited. The original full-precision MILO member has not been authenticated here.

OpenAI GPT models assisted exploration, programming, checking and drafting; Google Gemini models also participated in earlier research and checks. The paper discloses these roles. Correctness rests on the mathematical argument and exact certificates, not model agreement. Mathematical and reproducibility feedback is welcome.

## Licences

The paper and original documentation use [CC BY4.0](LICENSES/CC-BY-4.0.txt); original verification code uses [MIT](LICENSES/MIT.txt). See [scope](LICENSES/README.md). Third-party work is credited, not relicensed as our own.
