# Data and code availability

Repository designated by the authors:
https://github.com/1559204280-star/zh-kk-ai-corpus

Contact: gng@xju.edu.cn (Xinjiang University).

This package contains all five resource types: the 508-entry aligned terminology
table (`terminology/full508.csv`), historical prompt templates (`prompts/`),
text-free candidate-selection scores (`selection/candidate_scores.csv.gz`),
50 actual Chinese-Kazakh training examples (`examples/examples50.jsonl`),
and evaluation scripts (`evaluation/`). It also includes ranking-replay code,
source provenance, schemas and file checksums.

The authors authorized inclusion of the terminology table and 50 examples on
2026-11-05. Their original term/source and sentence strings are retained;
private sample IDs and ordering fields are removed from the example export.
The repository address is supplied, but upload and public access have not
been verified during this local preparation. No DOI is assigned.

Original Python code uses PolyForm Noncommercial 1.0.0. Authors' original
prompts, documentation, numerical score compilation and licensed contributions
to the example collection use CC BY-NC 4.0 to the extent applicable rights are
held. The terminology table retains source-specific upstream terms and is
excluded from the blanket original-material grant. See LICENSE and
terminology/LICENSE_STATUS.md. The package grants no additional commercial use.

The complete 49,998-pair training corpus, all other candidate text, private ID
mappings, human-reference test text and model weights remain excluded. Requests
concerning excluded materials may be sent to the contact above with the intended
use; any access remains conditional on relevant rights-holder permission.

Numerical replay reproduces ranking and selection from supplied scores. It does
not rerun model generation or establish semantic translation quality. The 50
examples are uncorrected synthetic training translations, not human references.

After this version is uploaded and public access is verified, the manuscript
can identify these five resource types at the repository URL above, with the
actual component-specific terms and excluded full-corpus scope specified.
