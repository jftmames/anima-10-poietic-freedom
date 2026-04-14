import csv
import glob
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from src.pipeline import eval_case


def main():
    rows = [eval_case(p) for p in glob.glob("data/case_files/**/*.json", recursive=True)]
    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/report.csv"
    columns = ["id", "domain", "title", "mdl_delta", "network_rupture", "L_star"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    print("Wrote", output_path, "with", len(rows), "rows.")


if __name__ == "__main__":
    main()
