# ANIMa-10: Poietic Freedom — Data & Code

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16923281.svg)](https://doi.org/10.5281/zenodo.16923281)
[![CI](https://github.com/jftmames/anima-10-poietic-freedom/actions/workflows/ci.yml/badge.svg)](https://github.com/jftmames/anima-10-poietic-freedom/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue.svg)](LICENSE-MIT)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](LICENSE-CC-BY-4.0)


This repository accompanies the paper **“Creative Freedom: Novelty, Non-Necessity, and Self-Determination Without Prior Rule.”**  
It provides a minimal, reproducible toolkit to audit **poietic acts** using the **Free\*** Diagnostic Protocol (FDP) and the **Poietic Index `L*`**.

> **Licensing:** Code under MIT (`LICENSE-MIT`). Data & documentation under CC BY 4.0 (`LICENSE-CC-BY-4.0`).

---

## Contents

- `src/` — Signals for **NO** (proxy MDL-Δ via compression) and **network rupture** (simple graph stats), plus `L*` utilities.
- `data/` — Minimal public-like examples and **one case file per domain** (craft, commerce, law, philosophy, painting, architecture, poetry, physics, mathematics, computing) + a computing control case.
- `scripts/` — Pipeline to compute signals and `L*` across case files.
- `docs/` — Data dictionary, minimal methods, preregistration stub.
- `paper/` — Place your LaTeX sources here (`Makefile` + `latexmkrc` included).
- `.github/workflows/ci.yml` — Basic CI (tests + pipeline on each push).
- `tests/` — Minimal unit tests.
- `outputs/` — Generated reports (e.g., `report.csv`).

---

## Quickstart

### A) GitHub Codespaces (no local install)
Open the repo in **Codespaces** and run:
```bash
make test
make pipeline
````

The pipeline writes `outputs/report.csv` with proxy signals and `L*`.

### B) Local (Python ≥ 3.10)

```bash
python -m pip install --upgrade pip
pip install numpy pandas networkx scipy matplotlib pytest
make test
make pipeline
```

> The provided signals are **proxies** for demonstration:
>
> * `mdl_delta`: zlib-compressed size change between pre/post corpora.
> * `network_rupture`: change in largest connected component + average clustering.
>
> Swap them for domain-grade metrics in your study (formal MDL, community/modularity, domain-controlled surprisal, etc.). See `docs/METHODS.md`.

### C) Streamlit demo

Launch an interactive app to explore case files or enter your own examples:

```bash
streamlit run streamlit_app.py
```

The app computes the proxy signals and `L*` for the selected inputs.

---

## Case File Schema (tl;dr)

Each case (`data/case_files/<domain>/<id>.json`) follows `docs/data_dictionary.md`:

* Stable ID: `anima:<domain>:<case_id>`
* `domain`, `title`, `locale`, `t0_interval`
* `predecessors_Ot`: 3–7 predecessors (the option set `O_t`)
* `closures_R`: doctrinal / material / discursive closures
* `evidence`: per-criterion (NO, ¬RC, NN, IF, Ctrl)
* `Lstar`: binary flags per criterion + `score`
* `corpora`: paths to `pre` / `post` plain texts
* `graphs`: paths to `pre` / `post` edge lists (CSV)

Run `make pipeline` to compute the proxy signals and aggregate outputs.

---

## Citing

Please cite the archived release on Zenodo:

> Fernández Tamames, J. (2025). **ANIMa-10: Poietic Freedom — Data & Code** (v1.0.0). Zenodo. [https://doi.org/10.5281/zenodo.16923281](https://doi.org/10.5281/zenodo.16923281)

You can also use `CITATION.cff` (GitHub will show a “Cite this repository” button).

---

## Contributing

Contributions are welcome:

* New or improved case files (`data/case_files/`) following the schema.
* Stronger methods in `src/` and matching tests.
* Clearer documentation and reproducible examples.

See `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` before opening a PR.

**Ethics & data:** public sources only; no personal/sensitive data.
Cite primary/secondary sources with persistent links/DOIs.

---

## Building the Paper

The `paper/` folder includes a `Makefile` and `latexmkrc` configured for **XeLaTeX + biber**.
If you have TeX tools available:

```bash
make -C paper
```

Otherwise, compile via your TeX environment of choice (Overleaf, etc.).

---

## Release & Zenodo Notes

1. Connect the GitHub repo to **Zenodo**.
2. Create a GitHub **Release** (e.g., `v1.0.0`).
3. Zenodo will archive it and mint a DOI. This README uses: **10.5281/zenodo.16923281**.
4. Keep the DOI in sync across `README.md`, `CITATION.cff`, and `.zenodo.json`.

---

## License

* **Code:** [MIT](LICENSE-MIT)
* **Data & Docs:** [CC BY 4.0](LICENSE-CC-BY-4.0)

---

*Maintainer:* José Fernández Tamames — ORCID: 0009-0007-8851-9833

```

