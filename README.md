# ANIMa-10: Poietic Freedom — Data & Code

This repository accompanies the paper *Creative Freedom: Novelty, Non-Necessity, and Self-Determination Without Prior Rule*.
It contains a minimal, reproducible toolkit to audit **poietic acts** using the Free* Diagnostic Protocol (FDP) and the Poietic Index `L*`.

> **Licensing**: Code under MIT (`LICENSE-MIT`). Data & docs under CC-BY-4.0 (`LICENSE-CC-BY-4.0`).

## Contents
- `src/`: Signals for NO (MDL-Δ proxy via compression; network rupture via graph stats) and `L*`.
- `data/`: Minimal public-data-like examples and one **case file per domain** (10 domains).
- `scripts/`: Pipeline to compute signals and `L*` over case files.
- `docs/`: Data dictionary, rubric summary, preregistration stub.
- `paper/`: Put your LaTeX sources here (Makefile included).
- `outputs/`: Reports produced by the pipeline.
- `.github/workflows/ci.yml`: Basic CI to run tests and pipeline on push.

## Quickstart (GitHub Codespaces or local)
```bash
# Run the pipeline
make pipeline

# Run tests
make test

# Compile the paper (needs TeX + biber)
make -C paper
