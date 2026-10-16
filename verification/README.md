# Verification

Run the three commands in the repository README from its root. The lower and upper sources contain their coefficient data; the Arena checker reads only arena/solution.json and arena/certificate.json. All proof calculations use Python standard-library integer and rational arithmetic. NumPy is not a dependency of these checkers; it was used only to reproduce the official Arena floating verifier locally.

The lower checker enforces115CPU seconds/175wall seconds; the upper30/55; the Arena checker45/65. Each caps address space at512MiB. Runtime depends on the machine. Assertions are essential and optimized modes are refused.

The lower calculation regenerates its integral bounds, checks80vertices,20closed rectangles and56elementary boxes, and prints exact L. The upper calculation checks4097signed events and prints exact U and the profile’s own variation. The upload checker certifies the distinct dyadic export, including its exact mass, box and all-real maximum. None is a search program.

The source-credit register refers to a larger historical working archive. That archive is not needed for the proofs and is not published here; paper/source_references.json supplies factual bibliographic metadata and source URLs. No raw upstream source or credentials are included.
