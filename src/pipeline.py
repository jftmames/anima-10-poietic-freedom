import json
import os
from typing import Dict, Any
from .lstar import l_star
from .mdl_delta import mdl_delta
from .network_rupture import load_edge_list_csv, rupture_score


def load_text(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def eval_case(case_path: str) -> Dict[str, Any]:
    """Load a case file and compute its metrics.

    The function guards against missing or malformed case files so the
    Streamlit demo can fail gracefully instead of raising a ``NameError`` or
    ``JSONDecodeError``.  When the case cannot be loaded an ``error`` key is
    returned for the caller to display.
    """

    try:
        with open(case_path, "r", encoding="utf-8") as f:
            case = json.load(f)
    except (OSError, json.JSONDecodeError):
        return {"error": f"Could not load case file: {case_path}"}

    cid = case.get("id")
    domain = case.get("domain")
    title = case.get("title")
    corp = case.get("corpora", {})
    graph = case.get("graphs", {})

    pre_text = load_text(corp.get("pre", ""))
    post_text = load_text(corp.get("post", ""))
    mdl = mdl_delta(pre_text, post_text) if pre_text and post_text else None

    pre_graph = graph.get("pre")
    post_graph = graph.get("post")
    if pre_graph and post_graph and os.path.exists(pre_graph) and os.path.exists(post_graph):
        G0 = load_edge_list_csv(pre_graph)
        G1 = load_edge_list_csv(post_graph)
        rupt = rupture_score(G0, G1)
    else:
        rupt = None

    scores = case.get("Lstar", {})
    L = l_star(scores) if scores else None
    return {
        "id": cid,
        "domain": domain,
        "title": title,
        "mdl_delta": mdl,
        "network_rupture": rupt,
        "L_star": L,
    }
