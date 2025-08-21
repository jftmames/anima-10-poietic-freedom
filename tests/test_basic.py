from src.lstar import l_star, DEFAULT_WEIGHTS
from src.mdl_delta import mdl_delta

def test_lstar_all_ones():
    scores = {k:1 for k in DEFAULT_WEIGHTS}
    assert abs(l_star(scores) - 1.0) < 1e-9

def test_mdl_delta_zero_on_empty():
    assert mdl_delta("", "") == 0.0
