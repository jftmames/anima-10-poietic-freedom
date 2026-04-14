import json
import os
from typing import Any, Dict

from .lstar import l_star
from .mdl_delta import mdl_delta
from .network_rupture import load_edge_list_csv, rupture_score


def load_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def _resolve_path(case_path: str, relative_or_abs_path: str) -> str:
    if not relative_or_abs_path:
        return ""
    if os.path.isabs(relative_or_abs_path):
        return relative_or_abs_path
    if os.path.exists(relative_or_abs_path):
        return os.path.normpath(relative_or_abs_path)
    return os.path.normpath(os.path.join(os.path.dirname(case_path), relative_or_abs_path))


def eval_case(case_path: str) -> Dict[str, Any]:
    with open(case_path, "r", encoding="utf-8") as f:
        case = json.load(f)

    cid = case.get("id")
    domain = case.get("domain")
    title = case.get("title")

    corp = case.get("corpora", {})
    graph = case.get("graphs", {})

    pre_text_path = _resolve_path(case_path, corp.get("pre", ""))
    post_text_path = _resolve_path(case_path, corp.get("post", ""))
    pre_graph_path = _resolve_path(case_path, graph.get("pre", ""))
    post_graph_path = _resolve_path(case_path, graph.get("post", ""))

    pre_text = load_text(pre_text_path)
    post_text = load_text(post_text_path)
    mdl = mdl_delta(pre_text, post_text)

    rupt = None
    if pre_graph_path and post_graph_path and os.path.exists(pre_graph_path) and os.path.exists(post_graph_path):
        g0 = load_edge_list_csv(pre_graph_path)
        g1 = load_edge_list_csv(post_graph_path)
        rupt = rupture_score(g0, g1)

    scores = case.get("Lstar", {})
    lstar_value = l_star(scores) if scores else None

    return {
        "id": cid,
        "domain": domain,
        "title": title,
        "mdl_delta": mdl,
        "network_rupture": rupt,
        "L_star": lstar_value,
    }
