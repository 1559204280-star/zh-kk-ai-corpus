# Fifty actual EqualFour corpus examples

`examples50.jsonl` contains 50 real Chinese-Cyrillic Kazakh sentence pairs from
the frozen 49,998-pair EqualFour-Top1 training corpus. The authors authorized
including these examples on 2026-11-05. The complete training corpus and human
reference test text are not distributed here.

## Fields

- `example_id`: public display ID E001-E050.
- `zh_source`: the original Chinese source string.
- `kk_translation`: the retained EqualFour synthetic target string.

The source and target strings are unchanged. Original record IDs, sample-order
values and private mappings are omitted. Before export, every pair and its
private original ID were checked against the frozen EqualFour corpus.

The examples retain the first 50 entries of an earlier prepared formal
500-item audit export; no quality-based reselection or correction was made.
They may contain translation errors. They are illustrative synthetic-training
examples, not human reference translations, a terminology gold set, or an
unbiased estimate of whole-corpus quality. The private audit export and ID
mapping remain undistributed.

The authors' licensed contributions to the sample collection are covered by
CC BY-NC 4.0 to the extent applicable rights are held; see LICENSE-DATA.md.
No further rights to whole course videos, other transcripts or excluded text
are granted. Third-party rights and applicable conditions remain in force.
The strings under `evaluation/demo` are separate software-test fixtures.
