# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
# ---

# %% [markdown]
# # 02 — Per-species η decomposition diagnostic
#
# For each of a small diagnostic set of species, decompose the GLMM linear
# predictor η at the SSP3-7.0 mid-term horizon (2030–2039) into its 10
# fixed-effect term contributions plus the species random intercept, at
# **both** substrates (HEALPix nside=64 and nside=128).
#
# This is the diagnostic that pinpoints which GLMM term is responsible for
# the cross-substrate η divergence per species. It is **not** the headline
# statistic of this repo — that lives in `03_variants.py`. It is the
# mechanistic evidence behind the framing.
#
# Output: `results/substrate_comparison_decomposition_2030_2039.txt`.

# %%
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Diagnostic species set: 4 most-divergent across substrates + 4 stable
# controls + 4 mid-range (chosen from the n_cells distribution).
DIAGNOSTIC_SPECIES = [
    # rank-divergent (high-impact, low-N)
    "norvegicus", "mendax", "jonellus", "sylvestris",
    # mid (n=5–10 cells)
    "pyrenaeus", "wurflenii", "mucidus", "mesomelas",
    # stable (n>20 cells)
    "hortorum", "lapidarius", "terrestris", "pratorum",
]

OUT = REPO_ROOT / "results" / "substrate_comparison_decomposition_2030_2039.txt"
OUT.parent.mkdir(parents=True, exist_ok=True)

cmd = [sys.executable, str(REPO_ROOT / "scripts" / "compare_substrates.py"),
       *DIAGNOSTIC_SPECIES, "--horizon", "2030_2039"]
print("Running:", " ".join(cmd))
proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
OUT.write_text(proc.stdout)
print(f"Wrote {OUT}  ({OUT.stat().st_size:,} bytes)")

# %% [markdown]
# ## How to read the output
#
# For each species block, the table reports — at each substrate — the
# per-cell **mean** value of:
#
# 1. The four raw climate predictors (TEI_bs, TEI_delta, PEI_bs, PEI_delta)
# 2. Their substrate-specific z-scores (sc_TEI_bs, sc_TEI_delta, etc.)
# 3. The contribution of each of the 10 GLMM terms to η, plus the species
#    random intercept (`species_RE`)
# 4. The total η.
#
# Lines flagged `<--` indicate a per-term contribution shift of more than
# 1 logit between substrates — the dominant drivers of divergence. Across
# the diagnostic set, the flagged term is almost always
# `sc_TEI_delta:sc_PEI_delta` — the interaction term that compounds
# substrate-specific standardisation quadratically when future predictors
# extrapolate outside the training distribution.
