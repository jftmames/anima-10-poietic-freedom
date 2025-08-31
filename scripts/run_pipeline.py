import glob
import os
import pandas as pd
from src.pipeline import eval_case

def main():
    rows = [eval_case(p) for p in glob.glob("data/case_files/**/**/*.json", recursive=True)]
    os.makedirs("outputs", exist_ok=True)
    pd.DataFrame(rows).to_csv("outputs/report.csv", index=False)
    print("Wrote outputs/report.csv with", len(rows), "rows.")


if __name__ == "__main__":
    main()
