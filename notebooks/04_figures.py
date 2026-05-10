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
# # 04 — Figures
#
# Generate the two main-result figures per horizon:
#
# 1. **Concordance heatmap** — Spearman ρ for variant × n_cells filter.
# 2. **Variant pair-plot** — per-species scatter of η_64 vs η_128 for each
#    of the five variants, points coloured by min(n_cells_64, n_cells_128).

# %%
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

env = {**os.environ, "MPLBACKEND": "Agg"}
for horizon in ("2020_2029", "2030_2039"):
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "plot_variant_concordance.py"),
           "--horizon", horizon]
    print(f"=== Horizon {horizon} ===")
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, env=env)

# %% [markdown]
# Outputs:
#
# - `figures/variant_concordance_2020_2029.png`
# - `figures/variant_concordance_2030_2039.png`
# - `figures/variant_pairs_2020_2029.png`
# - `figures/variant_pairs_2030_2039.png`
