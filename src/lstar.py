from __future__ import annotations

from typing import Dict, List

DEFAULT_WEIGHTS = {
    "NO": 0.30,
    "NOT_RC": 0.25,
    "NN": 0.20,
    "IF": 0.15,
    "Ctrl": 0.10,
}


def l_star(scores: Dict[str, int], weights: Dict[str, float] = None) -> float:
    if weights is None:
        weights = DEFAULT_WEIGHTS
    return float(sum(weights[k] * int(scores.get(k, 0)) for k in weights))


def cohen_kappa(r1: List[int], r2: List[int]) -> float:
    assert len(r1) == len(r2) and len(r1) > 0

    n = len(r1)
    agree = sum(1 for a, b in zip(r1, r2) if a == b)
    p0 = agree / n

    r1_yes = sum(r1) / n
    r2_yes = sum(r2) / n
    p_yes = r1_yes * r2_yes
    p_no = (1 - r1_yes) * (1 - r2_yes)
    pe = p_yes + p_no

    if pe == 1.0:
        return 1.0
    return (p0 - pe) / (1 - pe)
