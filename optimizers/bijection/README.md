# anonframework-optimizer-bijection

A **Bijection Learning** jailbreak optimizer for the
[anonframework](https://example.invalid) red-teaming framework.

> **Community port — not an official implementation.** This module is an
> unofficial re-implementation of Bijection Learning (Huang et al., Haize Labs)
> for anonframework. It is not affiliated with, endorsed by, or maintained by the
> original authors. See [ASSUMPTIONS.md](ASSUMPTIONS.md) for every deliberate
> deviation from the paper and reference code.

Bijection learning is a black-box, model-agnostic jailbreak: it randomizes a
bijective character map ("Language Alpha"), teaches the target model that map
in-context with a few encode/decode examples, then sends the harmful query
encoded under the same map. Capable models follow the encoding into the
encoded answer space, sidestepping refusal training that was only ever
trained on plain English. One anonframework run samples and tries one fresh random
bijection; multiple runs give best-of-N, as in the paper.

Reference: Huang, Li, Tang, "Endless Jailbreaks with Bijection Learning,"
[arXiv:2410.01294](https://arxiv.org/abs/2410.01294) (ICLR 2025, Haize Labs).
See [ASSUMPTIONS.md](ASSUMPTIONS.md) for the full paper-to-code mapping and
every deliberate departure.

## Install

```bash
python -m pip install -e "/path/to/anonframework-modules/optimizers/bijection"
```

## Usage

```python
from bijection_optimizer import BijectionOptimizer

# Auto-tunes codomain + fixed_size from the in-scope `model` observable
# (paper Table 1: digit codomain for stronger models, letter for weaker ones).
optimizer = BijectionOptimizer(max_attempts=6)

# Explicit configuration always wins over auto-tune.
optimizer = BijectionOptimizer(bijection_type="digit", fixed_size=8, num_digits=2)
```

Wire it into a `Controller` like any other anonframework optimizer — see the
framework's [architecture overview](https://example.invalid) and a
target's README (e.g. `anonframework-target-chatbot`) for a full `Controller.run()`
example.

## Behaviour notes

- **Single-turn, packed prompt.** Upstream can use multi-turn teaching;
  anonframework has no assistant-prefill primitive, so a multi-turn version would
  cost ~11x more model calls for no accuracy upside here, and this port stays
  single-turn by design (see ASSUMPTIONS.md).
- **Two-channel split when `system_prompt` is in scope**: the alphabet-table
  teaching content goes in the system prompt, the encoded query in the user
  message, matching the paper's stronger configuration.
- **Response-blind construction.** Bijection construction never depends on
  seeing the target's previous response (matches the paper); in
  response-visible settings, only the early-stop decision uses
  `RunEndEvent.evaluation.success`.
- `target_controllable_name` lets you point the optimizer at a non-`chatbot`
  target's user-message controllable by name.

## License

MIT for this port's code (see [LICENSE](LICENSE)). The upstream reference
implementation,
[`haizelabs/bijection-learning`](https://github.com/haizelabs/bijection-learning),
carries no LICENSE file; its authors granted the anonframework maintainers permission,
in private correspondence, to redistribute the ported material under MIT terms.
The bijection
construction/encode/decode ports and the teaching-intro prompt text are credited
in [`NOTICE`](NOTICE), and the MIT text applied to them is reproduced in
[`LICENSES/bijection-learning-MIT.txt`](LICENSES/bijection-learning-MIT.txt).
