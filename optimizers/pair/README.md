# anonframework-optimizer-pair

PAIR (Prompt Automatic Iterative Refinement) jailbreak optimizer for the
[anonframework](https://example.invalid) red-teaming framework.

> **Community port — not an official implementation.** This module is an
> unofficial re-implementation of PAIR (Chao et al.) for anonframework. It is not
> affiliated with, endorsed by, or maintained by the original authors. See
> [ASSUMPTIONS.md](ASSUMPTIONS.md) for every deliberate deviation from the
> paper and reference code.

PAIR is a query-efficient, black-box jailbreak method: an attacker LLM
iteratively refines an adversarial prompt against a target model, using a judge
to score each attempt and feeding the target's response back as the next
iteration's context.

## Install

```bash
python -m pip install -e "/path/to/anonframework-modules/optimizers/pair"
```

## Credits / upstream

This optimizer is a faithful reimplementation of **PAIR** (Prompt Automatic
Iterative Refinement) for the anonframework framework.

- **PAIR** - Chao et al., "Jailbreaking Black Box Large Language Models in
  Twenty Queries" (arXiv:2310.08419),
  https://github.com/patrickrchao/JailbreakingLLMs. MIT License, Copyright (c)
  2023 PAIR Team. The attacker system prompts, the GPT-judge prompt and
  `Rating: [[n]]` format, the init/feedback message formats, the GCG refusal
  keyword dictionary, and the runtime defaults are ported verbatim from this
  repository and are redistributed here under its MIT license.
- **Persuasion prompt examples** - the logical-appeal and authority-endorsement
  worked examples derive from Zeng et al., "How Johnny Can Persuade LLMs to
  Jailbreak Them" (arXiv:2401.06373), reaching this module through the PAIR
  repository.
- **Refusal dictionary** - the `gcg` judge's refusal-string list originates
  from GCG (Zou et al., arXiv:2307.15043,
  https://github.com/llm-attacks/llm-attacks, MIT, Copyright (c) 2023 Andy
  Zou), via PAIR.

Our anonframework integration code is MIT-licensed (see LICENSE and NOTICE).
