# Corpus-level evaluation

The CLI extracts the paper's metric calculation into a standalone script. It
does not generate translations, download models, or call paid APIs.

## Run

From the package root, in your own Python environment:

```sh
python -m pip install -r evaluation/requirements.txt
python evaluation/test_metrics.py
python evaluation/evaluate_metrics.py --predictions evaluation/demo/predictions.txt --references evaluation/demo/references.txt
```

For research predictions, replace the two input files. Each UTF-8 line must
correspond to the same test item in both files, in identical order. Do not
remove blank lines independently. No test-set text is bundled.

## Historical metric settings

- SacreBLEU 2.4.3; corpus-level scores, reported on a 0-100 scale.
- BLEU: case-sensitive, 13a tokenization, exponential smoothing, no effective order.
- chrF++: character order 6, word order 2, beta=2, case-sensitive, character whitespace excluded, effective-order smoothing.
- A single human reference per prediction.
- Historical decoding removed special tokens with `skip_special_tokens=True`
  and applied `.strip()` to each prediction. No extra lowercasing, stemming,
  transliteration, or evaluation cleaning was applied. Prepare inputs that way
  before using this CLI; the CLI itself removes only line terminators.

The original metric function snapshot has SHA256
`f7414d8efb5d8f80d3b78581646f2996c452acd6d2815a331085f7b2a45dc885`.
The wrapper retains its BLEU/CHRF constructor settings. The original internal
result key `chrf2` is named `chrf_plus_plus` here to make word_order=2 explicit.
The model/runtime provenance document records historical inference settings.

These scripts cover BLEU and chrF++, the two paper-table metrics. They do not
claim to reproduce COMET or training without the corresponding models and data.
