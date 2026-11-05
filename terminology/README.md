# Chinese-English-Russian-Kazakh terminology table

`full508.csv` contains the frozen aligned terminology table: 508 records,
344 distinct Chinese heads, and 346 distinct raw Chinese-Kazakh pairs.
It is included following the authors' release authorization of 2026-11-05.

The CSV retains the original ten fields and all original term strings.
Contributions are 202 AITD, 91 Google ML Glossary, and 215 GIST Chinese-English
source records linked to ISSAI English-Kazakh-Russian entries. These counts
are aligned records, not 508 independent concepts. The separate expansion
review queue is not included.

English names were normalized and exactly aligned. The links do not establish
contextual disambiguation, complete morphological analysis or human term accuracy.
A Chinese head may have multiple Kazakh alternatives. The generation prompts
use these as soft references and permit inflection in context.

## Files and reuse

- `full508.csv`: aligned entries, with source identifiers and alignment status.
- `schema.json`: definitions for its ten columns.
- `source_manifest.json`: upstream URLs, versions, source counts and release scope.
- `source_license_status.csv`: retained source-specific license evidence.
- `LICENSE_STATUS.md`: attribution and source-specific reuse limits.

This table incorporates third-party terminology. It is excluded from the
package-wide original-material CC BY-NC grant; source-specific upstream terms
remain applicable. The authors' authorization to include the table is recorded
separately from observed upstream notices and is not presented as a newly
verified universal license for the combined table. In particular, retain AITD
noncommercial/share-alike requirements and required source attribution.
