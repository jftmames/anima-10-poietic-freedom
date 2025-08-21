import json, glob, os, pandas as pd
from src.lstar import l_star, DEFAULT_WEIGHTS
from src.mdl_delta import mdl_delta
from src.network_rupture import load_edge_list_csv, rupture_score

def load_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def eval_case(case_path: str) -> dict:
    case = json.load(open(case_path, 'r', encoding='utf-8'))
    cid = case.get("id"); domain = case.get("domain"); title = case.get("title")
    corp = case.get("corpora", {}); graph = case.get("graphs", {})
    pre_text = load_text(corp.get("pre", "")); post_text = load_text(corp.get("post", ""))
    mdl = mdl_delta(pre_text, post_text) if pre_text and post_text else None
    if graph.get("pre") and graph.get("post"):
        G0 = load_edge_list_csv(graph["pre"]); G1 = load_edge_list_csv(graph["post"])
        rupt = rupture_score(G0, G1)
    else:
        rupt = None
    scores = case.get("Lstar", {})
    L = l_star(scores) if scores else None
    return {"id": cid, "domain": domain, "title": title, "mdl_delta": mdl, "network_rupture": rupt, "L_star": L}

def main():
    rows = [eval_case(p) for p in glob.glob("data/case_files/**/**/*.json", recursive=True)]
    os.makedirs("outputs", exist_ok=True)
    pd.DataFrame(rows).to_csv("outputs/report.csv", index=False)
    print("Wrote outputs/report.csv with", len(rows), "rows.")

if __name__ == "__main__":
    main()
