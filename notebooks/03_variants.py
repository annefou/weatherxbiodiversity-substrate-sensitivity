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
# # 03 — Five-variant cross-substrate concordance
#
# This is the **headline statistic** of this repo. For each species and
# horizon, compute five candidate per-species rankings:
#
# - (a) Full GLMM η, within-substrate standardisation
# - (b) Main-effects-only η, within-substrate standardisation
# - (c) Full η, shared CEA reference standardisation
# - (d) Mean future TEI (substrate-invariant physical metric)
# - (d2) Fraction of cells with TEI_future > 0.5
#
# Then compute Spearman ρ between nside=64 and nside=128 rankings at four
# minimum-cell-count filters: ≥1, ≥5, ≥10, ≥20.
#
# The headline finding: at n≥10, **(b) main-effects-only η** lifts ρ from
# +0.59 to **+0.97** (mid-term horizon). The substrate-invariant physical
# metric (d) hits ρ ≥ +0.66 at all sample sizes.
#
# Outputs (per horizon):
#
# - `results/variant_comparison_<horizon>.csv`
# - `results/variant_comparison_<horizon>.json`

# %%
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

for horizon in ("2020_2029", "2030_2039"):
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "compare_variants.py"),
           "--horizon", horizon, "--out-dir", str(REPO_ROOT / "results")]
    print(f"\n=== Horizon {horizon} ===")
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

# %% [markdown]
# ## What to look at
#
# - The Spearman heatmap (variant × n_cells filter) is the cleanest summary —
#   see `04_figures.py` for the visualisation.
# - The per-species CSV lets you inspect why a particular species' ranking
#   diverged: compare (a)_eta_64 vs (a)_eta_128 against the same species'
#   (b) main-effects-only η; if the gap shrinks, the interaction term was
#   the cause.
# - Variant (c) — shared CEA reference — barely improves on (a). This was
#   a refuted hypothesis: just rescaling future predictors at projection
#   time does not decouple the substrate, because the GLMM β coefficients
#   are themselves substrate-fit. To properly test (c) the GLMM would
#   need to be refit with shared standardisation, which is out of scope
#   for this repo.
