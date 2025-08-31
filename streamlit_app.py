import json

from typing import Dict, Any
from src.lstar import l_star
from .mdl_delta import mdl_delta
from .network_rupture import load_edge_list_csv, rupture_score


def load_text(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def eval_case(case_path: str) -> Dict[str, Any]:
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
