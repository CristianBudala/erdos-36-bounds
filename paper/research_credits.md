# Research credits and source register

## Relation to the paper

This register accompanies *Explicit two-sided bounds for Erdős’s minimum-overlap problem* by Cristian Budala. It separates sources used in the research from ingredients in the final proof. The paper itself retains the references needed to follow the argument; this companion records the broader credit without placing an execution history in the paper.

The audit covered61round input manifests,772unique configured paths,548frozen text/Python sources of at most120000bytes, and1241recorded report/supplement files totaling12006605bytes. The report scan produced no additional GitHub repository or arXiv paper leads beyond the source inventory. A bounded script inventory and new primary-source metadata checks supplement that record. This covers the documented research corpus, not unrecorded influences, every transitive software dependency or every model training source. All identified named proof predecessors are cited. Bibliographic checks are not re-proofs of the external authors’ certificates.

## Direct mathematical lineage

- **Ethan Patrick White:** finite-frequency Fourier/moment relaxation and the basic continuous lower-bound framework.
- **Liam Price:** public mean-bin, positive-part dual certificates and the upstream certificate package. Price’s attribution is supported by the problem owner’s proof-claim entry; the TeX proof note itself has no author byline.
- **Ruturaj R Raval:** central-bin refinement; his ownCITATION.cff and authorship statement identify him and his contribution. His retained material also credits the Station baseline and Price.
- **Haowen Deng:** weighted-Parseval central certificate. HisCITATION.cff gives family name Deng and given name Haowen. The larger noncentral number is not substituted for a global lower bound.
- **Bautista Machillari Dowguñiec:** subadditivity of the symmetrized overlap and integrated cuts, with exact-arithmetic validation. The byline and title were checked directly in the preserved primary PDF. These mechanisms are inherited, not claimed as new here.
- **Wassily Hoeffding and Colin McDiarmid:** the exponential-moment estimate and bounded-differences framework in the finite rounding argument.
- **Jan Kristian Haugland and P. Swinnerton-Dyer:** step-function upper constructions and the continuous/finite relationship; the Swinnerton-Dyer attribution is made through Haugland. The present finite transfers are proved explicitly and do not assume a limiting-value equivalence.
- **Leo Moser and Paul Erdős:** historical bound and the original problem. The Moser citation was checked in Haugland’s primary-paper bibliography; his original paper was not re-audited. The problem owner’s bibliography now resolves the original references as four distinct Erdős publications: *Some remarks on number theory*(1955), *Problems and results in additive number theory*(1956), *Some unsolved problems*(1961), and *Some of my forgotten problems in number theory*(1992). Bibliographical records were checked directly at <https://www.erdosproblems.com/bibs/Er55>, <https://www.erdosproblems.com/bibs/Er56>, <https://www.erdosproblems.com/bibs/Er61>, and <https://www.erdosproblems.com/bibs/Er92c>. The1955and1956items are different works, not competing dates for one title. Their original mathematical texts were not re-proved here.

Historical references in Price’s proof-note bibliography also credit **T. S. Motzkin, K. E. Ralston and J. L. Selfridge**, *Minimal overlap under translation*, Bulletin of the American Mathematical Society62(1956),abstract62T-245,p.558, and **S. Świerczkowski**, *On the intersection of a linear set with the translation of its complement*, Colloquium Mathematicum5(1958),185–197. These are indirect historical credits: their original texts were not re-examined and supply no unproved premise here.

## Other certificate and research contributions

**Sungyoon Kim and Mert Pilanci** developed dual-agent convex-relaxation work. **Ben Zanghi** maintains the Bochner/moment-matrix research repository, including the earlier exact512-cell upper certificate used in this workspace. **Nicolas Occis** maintains public lower-certificate and checking reports. Their public profiles verify those maintainer names; this does not establish individual authorship of every file. Claims of independent checking are attributed as reports, not presented as external human peer review of this paper. The documented Occis exterior/global-bound discrepancy is not imported into our proof.

**Stephen Chung, Wenyu Du and William J. Wesley** are the authors of the Station paper, which is part of the recorded source lineage and of Raval’s acknowledged upstream material. The structured-scaling work listed below was recorded background, not a premise of the final certificate.

## Upper construction lineage

The upper witness is incumbent-derived. Round0046starts from MILO’s512six-decimal replay values; the displayed sum is255999994/1000000rather than256. Adding six numerator units at coordinate219gives an exactly balanced, box-safe seed. This repaired member is not MILO’s original full-precision construction. The Round0047proposal explicitly refines U46; subsequent accepted members pass through U48, U49, the1024-cell refinements U50/U51 and the exact refinements U52–U54. The Round0049proposal reports a sequential-quadratic-programming initialization from the uncoupled U48base. Optimizer history is report-level provenance unless separately reproduced; the accepted coefficient vectors and their objectives are independently checked.

MILO’s full author list is **Prithwish Jana, Mononito Goswami, Hao Liu, Xinyu Li, Langlin Huang, Zhehui Huang, Zhishen Huang, Patrick Blöbaum, Anoop Deoras, Purak Jain, Nikos Kanakaris and Sahika Genc**. Their public replay is therefore credited both as source material and as a comparison, not merely mentioned as a competing score. The original full-precision MILO member remains unauthenticated. No latest-record claim follows from the reported-number comparison.

Arena public data and handles such as CodexProLong identify supplied comparison arrays, not verified individual human authors. A separately balanced version of Arena solution2507was checked in the audit; it is not the MILO record. AlphaEvolve and TTT-Discover figures appearing in source tables remain attributed reports unless their original constructions were separately checked. No individual identity is invented for these handles or systems.

## Instruments and numerical software

The paper derives its finite Fourier identity, polynomial moments, shared-complement estimate, interval-error bounds and finite transfers. Fubini, Taylor’s theorem, convexity, affine interpolation, Markov’s inequality and the union bound are standard tools, not claimed inventions. The numerical estimates are stated with their hypotheses and proved or reduced to explicit identities. Moore, Kearfott and Cloud are cited as standard interval-analysis background; this book was added in the editorial revision, not claimed as an original agent reading.

Historical branches include Bochner positivity, Fejér/Parseval constraints, Bernstein-basis positivity, polynomial moment/semidefinite relaxations, Farkas duality and Karush–Kuhn–Tucker conditions. They are not all ingredients of the final theorem. Standard background supplied here includes Bochner’s paper, Katznelson’s harmonic-analysis text, Lasserre’s moment work, Powers and Reznick on positive polynomials, and Nocedal and Wright on optimization. These background references must not be misrepresented as evidence of a specific unlogged consultation or as proof that an unsuccessful search rules out a method.

The standalone final checkers use only Python integer/rational arithmetic. Credit goes to **Guido van Rossum, the Python core contributors and the Python Software Foundation**, whose official history/license record identifies the project’s origins and collective contributions. The final checkers do not depend on NumPy, SciPy, SymPy, Arb or a solver.

The exploratory script inventory documents NumPy/SciPy calculations, SLSQP optimization, HiGHS linear programs, SymPy symbolic checks and CVXPY models with SCS/Clarabel selections. Import or solver selection is evidence of source-level tooling, not by itself of an executed successful search. The exact-versus-discovery distinction is retained in the inventory. Arb/python-flint, MPFI and mpmath interval calculations occur in predecessor or checking projects; they are credited as upstream numerical infrastructure, not falsely claimed as dependencies of the present standalone proof. Full bibliographic author lists follow, including the long software contributor lists rather than replacing them by et al.

## Main-paper references

### Moser

Leo Moser. *On the minimum overlap problem of Erdős*. Acta Arithmetica 5 (1959), 117--119. Historical bibliographic evidence: Haugland2016, References.

### Haugland1996

Jan Kristian Haugland. *Advances in the Minimum Overlap Problem*. Journal of Number Theory 58 (1996), 71--78. <https://doi.org/10.1006/jnth.1996.0064>

### Haugland2016

Jan Kristian Haugland. *The minimum overlap problem revisited*. arXiv:1609.08000 (2016). <https://arxiv.org/abs/1609.08000>

### White

Ethan Patrick White. *A new bound for Erdős’ minimum overlap problem*. Acta Arithmetica 208 (2023), 235-255. <https://doi.org/10.4064/aa220728-7-6>

### KimPilanci

Sungyoon Kim, Mert Pilanci. *AI-Assisted Discovery of Convex Relaxations via Dual Agents*. arXiv:2606.31182 (2026). <https://arxiv.org/abs/2606.31182>

### Price

Liam Price. *A Certified Lower Bound for Minimum Overlap*. Public proof note and certificate package (2026). <https://github.com/Leeham06972452/erdos-36-lower-bound>

### Raval

Ruturaj R Raval. *The Erdos Minimum-Overlap Constant Exceeds 0.38055925*. Public certificate, version 0.3.1 (2026). <https://doi.org/10.5281/zenodo.22647743>

### Deng

Haowen Deng. *A Sharper Certified Lower Bound for Erdős’ Minimum-Overlap Problem*. Public proof note and certificate (2026). <https://doi.org/10.5281/zenodo.22279894>

### Machillari

Bautista Machillari Dowguñiec. *A Certified Lower Bound for Erdős’s 36 (Minimum-Overlap Problem) via Subadditivity Constraints and Exact Arithmetic*. Manuscript, 19 September 2026. <https://drive.google.com/file/d/1ThaY0esdiK47E6jL2IGkh11UxkeqzRPy/view>

### Zanghi

Ben Zanghi (repository maintainer). *Erdős minimum overlap problem — improved lower bound on µ*. Public research repository (2026). <https://github.com/bzanghi/erdos-minimum-overlap-bochner>

### Occis

Nicolas Occis (repository maintainer). *A certified lower bound for Erdős’s minimum-overlap problem*. Public certificate and checking reports (2026). <https://github.com/occisn/erdos-36-certified-lower-bound>

### Station

Stephen Chung, Wenyu Du, William J. Wesley. *Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment*. arXiv:2608.23691 (2026). <https://arxiv.org/abs/2608.23691>

### MILO

Prithwish Jana, Mononito Goswami, Hao Liu, Xinyu Li, Langlin Huang, Zhehui Huang, Zhishen Huang, Patrick Blöbaum, Anoop Deoras, Purak Jain, Nikos Kanakaris, Sahika Genc. *MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution*. arXiv:2609.38349 (2026). <https://arxiv.org/abs/2609.38349>

### Hoeffding

Wassily Hoeffding. *Probability Inequalities for Sums of Bounded Random Variables*. Journal of the American Statistical Association 58 (1963), 13-30. <https://doi.org/10.1080/01621459.1963.10500830>

### McDiarmid

Colin McDiarmid. *On the method of bounded differences*. Surveys in Combinatorics, 1989  (1989), 148-188. <https://doi.org/10.1017/cbo9781107359949.008>

### Interval

Ramon E. Moore, R. Baker Kearfott, Michael J. Cloud. *Introduction to Interval Analysis*.   (2009). <https://doi.org/10.1137/1.9780898717716>

### Python

Guido van Rossum, the Python core contributors, and the Python Software Foundation. *Python 3: History and License*. Software documentation. <https://docs.python.org/3/license.html>

## Software and historical-method references

### numpy

Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, Travis E. Oliphant. *Array programming with NumPy*. Nature, 585, 357-362, 2020. <https://doi.org/10.1038/s41586-020-2649-2>.

### scipy

Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, SciPy 1.0 Contributors, Aditya Vijaykumar, Alessandro Pietro Bardelli, Alex Rothberg, Andreas Hilboll, Andreas Kloeckner, Anthony Scopatz, Antony Lee, Ariel Rokem, C. Nathan Woods, Chad Fulton, Charles Masson, Christian Häggström, Clark Fitzgerald, David A. Nicholson, David R. Hagen, Dmitrii V. Pasechnik, Emanuele Olivetti, Eric Martin, Eric Wieser, Fabrice Silva, Felix Lenders, Florian Wilhelm, G. Young, Gavin A. Price, Gert-Ludwig Ingold, Gregory E. Allen, Gregory R. Lee, Hervé Audren, Irvin Probst, Jörg P. Dietrich, Jacob Silterra, James T Webber, Janko Slavič, Joel Nothman, Johannes Buchner, Johannes Kulick, Johannes L. Schönberger, José Vinícius de Miranda Cardoso, Joscha Reimer, Joseph Harrington, Juan Luis Cano Rodríguez, Juan Nunez-Iglesias, Justin Kuczynski, Kevin Tritz, Martin Thoma, Matthew Newville, Matthias Kümmerer, Maximilian Bolingbroke, Michael Tartre, Mikhail Pak, Nathaniel J. Smith, Nikolai Nowaczyk, Nikolay Shebanov, Oleksandr Pavlyk, Per A. Brodtkorb, Perry Lee, Robert T. McGibbon, Roman Feldbauer, Sam Lewis, Sam Tygier, Scott Sievert, Sebastiano Vigna, Stefan Peterson, Surhud More, Tadeusz Pudlik, Takuya Oshima, Thomas J. Pingel, Thomas P. Robitaille, Thomas Spura, Thouis R. Jones, Tim Cera, Tim Leslie, Tiziano Zito, Tom Krauss, Utkarsh Upadhyay, Yaroslav O. Halchenko, Yoshiki Vázquez-Baeza. *SciPy 1.0: fundamental algorithms for scientific computing in Python*. Nature Methods, 17, 261-272, 2020. <https://doi.org/10.1038/s41592-019-0686-2>.

### sympy

Aaron Meurer, Christopher P. Smith, Mateusz Paprocki, Ondřej Čertík, Sergey B. Kirpichev, Matthew Rocklin, AMiT Kumar, Sergiu Ivanov, Jason K. Moore, Sartaj Singh, Thilina Rathnayake, Sean Vig, Brian E. Granger, Richard P. Muller, Francesco Bonazzi, Harsh Gupta, Shivam Vats, Fredrik Johansson, Fabian Pedregosa, Matthew J. Curry, Andy R. Terrel, Štěpán Roučka, Ashutosh Saboo, Isuru Fernando, Sumith Kulal, Robert Cimrman, Anthony Scopatz. *SymPy: symbolic computing in Python*. PeerJ Computer Science, 3, e103, 2017. <https://doi.org/10.7717/peerj-cs.103>.

### highs

Q. Huangfu, J. A. J. Hall. *Parallelizing the dual revised simplex method*. Mathematical Programming Computation, 10, 119-142, 2017. <https://doi.org/10.1007/s12532-017-0130-5>.

### lasserre

Jean B. Lasserre. *Global Optimization with Polynomials and the Problem of Moments*. SIAM Journal on Optimization, 11, 796-817, 2001. <https://doi.org/10.1137/s1052623400366802>.

### scs

Brendan O’Donoghue, Eric Chu, Neal Parikh, Stephen Boyd. *Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding*. Journal of Optimization Theory and Applications, 169, 1042-1068, 2016. <https://doi.org/10.1007/s10957-016-0892-3>.

### arb

Fredrik Johansson. *Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic*. IEEE Transactions on Computers, 66, 1281-1292, 2017. <https://doi.org/10.1109/tc.2017.2690633>.

### mpfi

Nathalie Revol, Fabrice Rouillier. *Motivations for an Arbitrary Precision Interval Arithmetic and the MPFI Library*. Reliable Computing, 11, 275-290, 2005. <https://doi.org/10.1007/s11155-005-6891-y>.

### cvxpy

Steven Diamond, Stephen Boyd. *CVXPY: A Python-Embedded Modeling Language for Convex Optimization*. JMLR17(83),1–5(2016). <https://www.jmlr.org/papers/v17/15-408.html>.

### clarabel

Paul J. Goulart, Yuwen Chen. *Clarabel: An interior-point solver for conic programs with quadratic objectives*. . <https://arxiv.org/abs/2405.12762>.

### slsqp

Dieter Kraft. *A software package for sequential quadratic programming*. Technical Report DFVLR-FB88-28(1988). <https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html>.

### optimization

Jorge Nocedal, Stephen J. Wright. *Numerical Optimization*. Springer Series in Operations Research and Financial Engineering, 2006. <https://doi.org/10.1007/978-0-387-40065-5>.

### harmonic

Yitzhak Katznelson. *An Introduction to Harmonic Analysis*. 2004. <https://doi.org/10.1017/cbo9781139165372>.

### bochner

S. Bochner. *Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse*. Mathematische Annalen, 108, 378-410, 1933. <https://doi.org/10.1007/bf01452844>.

### positivepolynomials

Victoria Powers, Bruce Reznick. *Polynomials that are positive on an interval*. Transactions of the American Mathematical Society, 352, 4677-4692, 2000. <https://doi.org/10.1090/s0002-9947-00-02595-2>.

### structured_scaling

Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Rahul Thapa, Caiyin Yang, Chang Su, Rui Yang, Ruihua Liu, Rundao Li, Zeyu Li, Pengwei Sun, Chong Gao, Dachao Ding, Guangrong He, Miaolei Zhang, Lina Sun, Wenyang Wang, Yuchen Zhong, Zhuohao Shen, Puheng Li, Pan Lu, Bianxiao Cui, Di He, Jianzhu Ma, Junfeng Li, Hexi Baoyin, Yejin Choi, Stefano Ermon, Xiaowen Chu, Tongyang Li, Yuzhi Xu, James Zou. *Structured Scaling of AI Discovery Across Diverse Scientific Domains*. arXiv:2604.19341,2026. <https://arxiv.org/abs/2604.19341>.

### Upstream semidefinite-certification method

Christian Jansson, Denis Chaykin and Christian Keil. *Rigorous Error Bounds for the Optimal Value in Semidefinite Programming*. SIAM Journal on Numerical Analysis46,180–200(published online2007;volume46,2008). <https://doi.org/10.1137/050622870>. This method is explicitly identified in Zanghi’s predecessor validation. It is credited as upstream methodology, not asserted to be used by our standalone checkers.

### Additional upstream software collectives

The **mpmath developers** (<https://mpmath.org>), **python-flint contributors** (<https://python-flint.readthedocs.io>), and **FLINT development team** (<https://flintlib.org>) are credited as upstream software collectives. Their libraries occur in the predecessor/checking ecosystem; they are not dependencies of the two standalone checkers. Individual contributor lists for these transitive projects were not separately audited, so no invented personal author list is supplied.

## Evidence, limits and redistribution

Machine-readable evidence is under data/preprint_revision_sources/: citation metadata, DOI/API responses, primary READMEs and CFF files, the author register, source-path and import inventories, named-instrument inventory and upper-lineage excerpts. The evidence files record source URLs and hashes; the main retrieval logs also record access times. Bibliographic corrections and unsuccessful searches are retained in the private audit note rather than included as references.

Repository and archived material have distinct licenses. Credit is not redistribution permission. In particular, Raval’s provenance states that Price’s unlicensed source was hash-pinned but not redistributed at the audited snapshot; do not copy that upstream code into a release without checking permission. No upstream code was added to this revision’s release files.

This register is intended to credit the documented human work honestly. It does not claim exhaustive priority, approval by the cited authors, complete human peer review or completeness beyond the stated source inventory. Unknown contributor identities and missing original source data are not filled in by inference. AI assistance is disclosed separately and no model is listed as a human author.

## Sources newly consulted for submission preparation

Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao, Adam Zsolt Wagner. *Mathematical exploration and discovery at scale*. arXiv:2511.02864. <https://arxiv.org/abs/2511.02864>. The official Arena problem identifies its task as Problem6.5of this work. It is credited for the benchmark/verifier context newly inspected during export preparation, not retrospectively claimed as a premise of the original proof.

The Erdős Problems database was created by **Thomas Bloom**, as stated in its FAQ; its contributors, including the additional assistance credited to **Terence Tao** on problem36, are acknowledged for the curated bibliographic information. This is not an endorsement or examination of this paper by them.
