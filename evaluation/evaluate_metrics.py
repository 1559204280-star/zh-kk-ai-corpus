"""Reproduce the paper's corpus BLEU and chrF++ calculation; no model calls."""
import argparse
import json
from pathlib import Path
import sacrebleu

EXPECTED_VERSION = "2.4.3"

def compute_metrics(predictions, references):
    if sacrebleu.__version__ != EXPECTED_VERSION:
        raise RuntimeError("Use the pinned environment: pip install -r evaluation/requirements.txt")
    if not predictions or len(predictions) != len(references):
        raise ValueError("Predictions and references must have the same nonzero line count")
    predicted = [str(value) for value in predictions]
    reference = [str(value) for value in references]
    bleu_metric = sacrebleu.metrics.BLEU(tokenize="13a")
    chrf_metric = sacrebleu.metrics.CHRF(word_order=2)
    bleu = bleu_metric.corpus_score(predicted, [reference])
    chrf = chrf_metric.corpus_score(predicted, [reference])
    return {
        "rows":len(predicted), "bleu":float(bleu.score), "chrf_plus_plus":float(chrf.score),
        "bleu_signature":str(bleu_metric.get_signature()),
        "chrf_signature":str(chrf_metric.get_signature()),
        "sacrebleu_version":sacrebleu.__version__,
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions",type=Path,required=True)
    parser.add_argument("--references",type=Path,required=True)
    args=parser.parse_args()
    # Remove line terminators only. Do not silently change case, spelling, or spacing.
    predictions=args.predictions.read_text(encoding="utf-8").splitlines()
    references=args.references.read_text(encoding="utf-8").splitlines()
    print(json.dumps(compute_metrics(predictions,references),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
