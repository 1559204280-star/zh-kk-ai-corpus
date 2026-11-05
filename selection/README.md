# EqualFour numerical selection replay

This directory contains the historical four signal scores and the EqualFour selection for the complete candidate pools used in the study. The score table contains no Chinese source text, Kazakh translation text, course titles, original record IDs or original candidate IDs.

## Files and scope

- `candidate_scores.csv.gz`: 226,477 distinct candidate rows from 49,999 complete source pools. Each pool represents seven route labels after exact raw-target-string deduplication. All origins of an identical translation are retained.
- `reproduce_selection.py`: a Python 3 standard-library program that independently recalculates the relative ranks, equally weighted scores, tie resolution and winning candidate IDs.
- `schema.csv`: column definitions and data types.
- `protocol.json`: the frozen aggregation and tie-breaking rules.
- `verification_summary.json`: expected counts, primary origins and the score-file checksum.

The `training_included` flag identifies the 49,998 source sentences used for downstream training. A complete pool excluded from training is retained for transparency. One of the original 50,000 source records lacked a complete seven-route pool and is absent from this table. Public source numbers are pseudonymous sequence labels; the original ID mapping is not distributed.

The numeric export was reconstructed from frozen historical scores. It is not a byte-for-byte copy of the historical ranked JSON file. No translation generation or model scoring was repeated. Before export, all 49,998 training winners were checked against the frozen EqualFour corpus, including source text, target text, course and order. All primary-origin counts and the 6,735 composite-score ties matched the historical selection contract. Across 123,516 duplicate-route occurrences, all four scores for identical target strings were exactly equal, so no score aggregation across differing duplicate scores was required.

## Run

From this directory:

```sh
python reproduce_selection.py
```

The program verifies every released rank, total score, position and selected flag and prints `PASSED` with the expected source and origin counts. No model, API key, network access or third-party Python dependency is needed.

To save the reconstructed winning IDs as a new CSV:

```sh
python reproduce_selection.py --output reconstructed_winners.csv
```

The output path must not already exist. The script verifies the checksum of the frozen score file; changing the data invalidates this release check.

## Numerical rules

The four signals are reference-free WMT23 COMET-QE (`qe`), SONAR cosine similarity (`cosine`), the Qwen3-Reranker yes-logit minus no-logit score (`qwen`), and the standard SONAR margin ratio with k=4 (`margin`). Higher raw values are better for each signal. The margin is the ordinary all-pool ratio; the unused leave-origin-out diagnostic is not exported.

Within each source pool of m distinct target strings, candidates receive zero-based average ranks from low to high. For m > 1, each normalized rank equals the average zero-based rank divided by m-1. Every normalized rank is 0.5 when m=1. EqualFour averages the four normalized ranks with weights 0.25 each.

The replay program computes twice the average rank as an integer. This keeps exact composite-score ties intact. If totals tie, prefer the higher raw QE score, then this fixed origin order:

```text
P1, T1, T2, T3_full508, F1, F2, N1
```

This same order assigns the primary origin of an identical translation with multiple origins. Origin counts are therefore attribution under a fixed rule, not independent model win rates. Raw numeric values are exported at full Python float round-trip precision, not rounded to the paper's two decimal places.

## Interpretation and limits

This release permits numerical reproduction of the candidate ranking and selection from supplied scores. Without source and target text, it does not permit independent rerunning of translation generation, model scoring, or the original string deduplication. Numerical reproducibility is not human validation of translation quality. Cosine and margin share a SONAR representation and are not independent quality votes. The Qwen logit difference is not a calibrated probability of translation correctness.

Reuse terms and the release status are documented at the package root. This is a local release candidate until the authors publish and identify a fixed version.
