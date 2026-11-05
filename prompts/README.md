# Historical prompts and request configuration

These files preserve the prompts and settings retained for Chinese-to-Cyrillic-Kazakh candidate generation and Qwen reranking. They are research records, not new requests. Reading or assembling a template does not call an API.

## Files

- `system_zh.txt`: exact shared DeepSeek system instruction.
- `t1_zh.txt`, `t2_zh.txt`, `t3_zh.txt`: exact per-style instructions.
- `t3_hint_zh.txt`, `t3_term_line_template.txt`: exact terminology-reference header and the documented line format.
- `translation_user_no_terms_template.txt`, `translation_user_with_terms_template.txt`: user-message structure without/with the optional T3 reference block.
- `assembly_rules.json`: source matching, option grouping, separators and placeholder rules.
- `deepseek_generation_config.json`: actual requested alias, endpoint, decoding settings, client-recorded time windows and historical reuse.
- `qwen_instruction.txt`, `qwen_chat_template.txt`: exact custom faithfulness instruction and complete serialized wrapper. Qwen uses the yes-minus-no logit difference for ranking.
- `../docs/model_and_runtime_provenance.json`: content fingerprints, selected runtime details and explicit gaps in the retained historical evidence.

## Exact prompt assembly

The Chinese prompt wording is intentionally retained: translating these instructions into English would produce a different request. Braced names in template files are placeholders for documentation. Do not send them literally. Constant files have no artificial terminal newline; the Qwen wrapper's own terminal newlines are preserved.

For DeepSeek, send two messages: the system constant, then a user message formed by joining the style instruction, the optional terminology block, `中文：` plus `source.strip()`, and `哈萨克语：` with exactly two newlines between present parts. Omit the optional part entirely when no terms apply. Join terminology lines with one newline. Multiple distinct options for one head are joined with ` / ` and followed by `（按语境选择一种）`; a single option has no suffix. Do not rewrite or split the source glossary cell values during this assembly.

Chinese matching uses longest-first non-overlapping literal spans; each selected head is injected once per source. All associated distinct Kazakh cell values are supplied for context-dependent selection. The reference is soft guidance, not a requirement to use a contextually inappropriate form. Inflection is permitted by the instruction. The aligned terminology entries are a separately controlled resource; these prompt files do not grant rights to redistribute that table.

## Historical scope and limitations

T1/T2/T3 use temperatures 0.0/0.8/0.7 and top-p 1.0/0.9/0.9, respectively, with a 512-token output limit and thinking disabled. No request seed field was sent. For expansion to 50,000 sources, the first 10,000 sources were reused; the next 40,000 used concurrency 4. The first 1,000 retained T3 outputs combine 194 full508 regenerations with 806 reused original T3 outputs. Thus the templates do not imply that every retained output was freshly generated with an identical full508 prompt.

The recorded API alias is `deepseek-flash`. An immutable provider-side revision and system fingerprint were not retained. The reported service name is based on historical invocation dates and the retained provider timeline. The timestamps identify when the client wrote records, not provider-generated timestamps. Repeating the same alias in the future is not guaranteed to recover identical output.

The original complete system/user prompt, immutable model revision and decoding settings were not established for Pengcheng P1 or the legacy GPT-labeled automatic review. No substitute prompt has been invented for them. NLLB, SONAR and QE-Fusion do not use a chat-generation prompt of the kind used by DeepSeek. Two automatic review runs must not be described as independent human judgments.

No course text, original response, private file location, task receipt, API credential or model weight is distributed here. These are local release-candidate materials; this directory does not assert that a repository has been published or that third-party permissions have been obtained.
