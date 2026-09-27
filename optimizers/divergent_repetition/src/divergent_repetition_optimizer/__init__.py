"""Divergent-repetition (repeat-a-word data-extraction) optimizer for anonframework.

Ported from garak (garak/probes/divergence.py).
"""

from divergent_repetition_optimizer.optimizer import (
    DivergentRepetitionOptimizer,
    build_prompts,
)

__all__ = ["DivergentRepetitionOptimizer", "build_prompts"]
