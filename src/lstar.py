from __future__ import annotations
from typing import Dict, List
import numpy as np

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
    r1 = np.array(r1); r2 = np.array(r2)
    p0 = (r1 == r2).mean()
    p_yes = (r1.mean()) * (r2.mean())
    p_no  = (1 - r1.mean()) * (1 - r2.mean())
    pe = p_yes + p_no
    if pe == 1.0: return 1.0
    return (p0 - pe) / (1 - pe)
