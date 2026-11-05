# Reproducibility materials for a Chinese–Cyrillic Kazakh AI-domain corpus

Version: **0.2.0**. Metadata and license decisions: 2026-11-05.

**Authors:** Mingyuzhe Huang; Gulinigeer Abudouwaili; Changlong Xu.  
**Affiliation:** Xinjiang University.  
**Correspondence:** gng@xju.edu.cn.  
**Repository:** https://github.com/1559204280-star/zh-kk-ai-corpus

These resources accompany the manuscript *Construction and Evaluation of a
Chinese-Kazakh Parallel Corpus in the Artificial Intelligence Domain*.
The repository address and author metadata were supplied by the authors.
Public upload and access have not been verified during this local preparation.
No DOI has been assigned. Original Python code uses PolyForm Noncommercial
1.0.0; original prompts, documentation and numerical score compilation use
CC BY-NC 4.0. Commercial use is not granted under these terms. See `LICENSE`,
`LICENSE-CODE.md`, `LICENSE-DATA.md` and `LICENSE_STATUS.md` for scope.
Following the authors' 2026-11-05 authorization, this version includes the
508-entry terminology table and 50 real EqualFour examples. Source-specific
terminology terms are preserved. The full training corpus and human-reference
test text remain excluded.

## Suggested citation

Mingyuzhe Huang, Gulinigeer Abudouwaili, and Changlong Xu (2026).
Reproducibility materials for a Chinese-Cyrillic Kazakh AI-domain corpus.
Version 0.2.0. https://github.com/1559204280-star/zh-kk-ai-corpus

## Resource index

| Material | Location | Included scope |
| --- | --- | --- |
| Historical prompts and API parameters | `prompts/` | Exact retained DeepSeek instructions, T3 assembly rules, Qwen wrapper, request settings and recorded time windows |
| Model, software and training provenance | `docs/model_and_runtime_provenance.json` | Available file fingerprints, versions, settings, hardware, runtimes and explicit historical evidence gaps |
| Candidate-selection scores | `selection/candidate_scores.csv.gz` | Text-free scores and selections for 49,999 complete source pools and 226,477 deduplicated candidates; 49,998 sources marked for training |
| Numerical selection replay | `selection/reproduce_selection.py` | Relative ranks, equal weighting, deterministic tie resolution and expected-count verification |
| BLEU and chrF++ evaluation | `evaluation/` | Standalone script pinned to SacreBLEU 2.4.3, tests, synthetic fixtures and numerical verification |
| Terminology table and metadata | `terminology/full508.csv` | 508 aligned entries plus source inventory, schema and source-specific license evidence |
| Actual corpus examples | `examples/examples50.jsonl` | 50 real frozen EqualFour pairs; original IDs omitted; source and target text unchanged |
| Data and code availability | `docs/AVAILABILITY.md` | Repository, contact, noncommercial licenses and restricted components |

## Candidate routes

- P1: retained translations from the external Pengcheng Starling service.
- N1: translations from NLLB-200-3.3B.
- T1/T2: DeepSeek candidates with faithful/natural-translation instructions.
- T3_full508: the retained terminology-reference route. The first 1,000
  sources include 194 full508 regenerations and 806 reused earlier T3 outputs;
  not every retained output was newly generated with an identical full508 prompt.
- F1: QE-Fusion using T1/T2/T3; F2: QE-Fusion using T1/T2/T3/P1.
- EqualFour-Top1: one candidate selected per source after exact target-string
  deduplication and within-source relative-rank averaging of QE, SONAR cosine,
  Qwen logit difference and SONAR margin, each with weight 0.25.

The original source freeze contains 50,000 records. One source lacks a complete
seven-route pool, leaving 49,999 complete pools. A further prior matched-training
exclusion leaves 49,998 training sources. Both counts are preserved explicitly
in the score export. Do not treat route count as the number of distinct target
strings: identical translations retain all of their route labels in `origins`.

## Quick numerical replay

From the extracted package root, with Python 3:

```sh
python selection/reproduce_selection.py
```

No model weights, API credentials, network access or third-party Python
packages are required for this replay. It checks every rank, weighted score,
selection position and winner flag, plus the frozen table checksum and counts.
An optional new output file can be requested with `--output winners.csv`.

The table preserves raw score precision. Composite ties are resolved by higher
raw QE, then fixed route priority; full rules are in `selection/protocol.json`.
All 49,998 training winners were checked against the frozen EqualFour corpus,
including source, target, course and order. The numerical export is a
reconstruction from retained historical scores, not a byte-identical copy of
the original ranked JSON file. No models were rerun to create it.

## Lexical evaluation

```sh
python -m pip install -r evaluation/requirements.txt
python evaluation/test_metrics.py
python evaluation/evaluate_metrics.py --predictions evaluation/demo/predictions.txt --references evaluation/demo/references.txt
```

The demo consists only of newly written synthetic software-test strings; it
is not a course sample, human assessment or model-performance result. The
standalone script reproduced the frozen P1 and F1 2,000-item BLEU and chrF++
scores and signatures to an absolute tolerance of 1e-9. That check is recorded
in `evaluation/verification.json`; the original test texts are not distributed.
BLEU uses 13a tokenization. chrF++ uses character order 6, word order 2 and beta 2.
The evaluation README specifies case, smoothing and post-processing details.

## Scope and limitations

This package supports **numerical replay from supplied scores**, not an
independent rerun of generation, model scoring or raw-string deduplication.
The text-free table cannot establish translation adequacy. SONAR cosine and
margin share representations, and the Qwen score is not a calibrated quality
probability. Availability of scripts does not reproduce the full training run.

Chinese wording in prompt files is intentional because translating the
instructions would change the historical requests. The recorded DeepSeek API
alias is `deepseek-flash`; no immutable backend revision was retained. Missing
Pengcheng and legacy GPT prompt/version details are marked as unknown instead
of being reconstructed speculatively. No model weights are included.

The included terminology table has 508 aligned records covering 344 Chinese
heads and 346 distinct raw Chinese-Kazakh pairs. It retains source-specific
reuse terms. The package also includes 50 actual synthetic-training examples.
All five resource types are now present in this upload package; this does not
assert that they have already been uploaded or made publicly accessible.
The examples are uncorrected training outputs, not human-reference translations.

## Integrity and release checklist

`manifest.json` inventories the payload. `SHA256SUMS.txt` hashes every file in
this package except the checksum file itself. The repository URL, author order, affiliation and contact are filled.
The original-material noncommercial licenses are specified. Before publication,
resolve any permissions needed for additional text releases and verify
repository access.
Do not claim a public release before the relevant files can be accessed.
