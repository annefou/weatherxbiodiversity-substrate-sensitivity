# weatherxbiodiversity-substrate-sensitivity

[![CI](https://github.com/annefou/weatherxbiodiversity-substrate-sensitivity/actions/workflows/ci.yml/badge.svg)](https://github.com/annefou/weatherxbiodiversity-substrate-sensitivity/actions/workflows/ci.yml)
[![Jupyter Book](https://github.com/annefou/weatherxbiodiversity-substrate-sensitivity/actions/workflows/jupyter-book.yml/badge.svg)](https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20113786.svg)](https://doi.org/10.5281/zenodo.20113786)
[![FAIR4RS](https://img.shields.io/badge/FAIR4RS-conformant-brightgreen)](docs/fair4rs-checklist.md)
[![FORRT](https://img.shields.io/badge/FORRT-replication-blue)](https://forrt.org/)

> **Substrate-sensitivity diagnostic for TEI-based extirpation projection.**
> Per-species ranking under future climate is grid-coupled at the projection step. Here is the mechanism, and three principled fixes.

This repository is a **methodological follow-up** to two single-substrate replications of Soroye et al. 2020 ([10.1126/science.aax8591](https://doi.org/10.1126/science.aax8591)) for Iberian *Bombus* under DestinE Climate DT SSP3-7.0:

| Substrate | Repo | Purpose |
|---|---|---|
| HEALPix nside=64 (~92 km) | [`weatherxbiodiversity-projection`](https://github.com/annefou/weatherxbiodiversity-projection) | canonical replication |
| HEALPix nside=128 (~46 km) | [`weatherxbiodiversity-projection-nside128`](https://github.com/annefou/weatherxbiodiversity-projection-nside128) | resolution extension |

Both single-substrate Outcomes are **Substrate-robust**: the GLMM coefficient on `sc_TEI_delta` is positive, large, and credible at all three pixelisations (CEA, nside=64, nside=128) — within ±30%. **Soroye's central biological claim replicates on Iberian *Bombus*.**

But when the same GLMM is asked to **project** to future climate, per-species rankings diverge across substrates by 1–9 logits. This repo asks: why does that happen, and how should it be done properly?

## Headline finding

The substrate-coupling at projection time is **not** caused by per-species random-effect refit (substrate-stable, ΔRE ≤ 0.6 logits) or by per-species niche-limit refit (modest, ΔT_range = 0–3°C). It is caused by **two mechanisms acting together**:

1. **Per-species sample size at projection time.** Below ~10 occupied + active cells per substrate, per-cell extrapolation noise dominates the species mean η, regardless of which projection variant is used.
2. **The GLMM interaction term `sc_TEI_delta:sc_PEI_delta` compounds substrate-specific standardisation quadratically when future predictors extrapolate 2–4σ outside the training distribution.** The same physical climate signal z-scores to opposite tails of the standardised distribution under each substrate's local (μ, σ); the interaction term scales as the product, amplifying the divergence.

## Recommended reporting protocol

For any future TEI-based extirpation projection that compares across substrates:

1. **Report only on species with ≥ 10 occupied + active cells per substrate.**
2. **Drop the GLMM interaction terms at projection time** — keep them in the fit, but use main-effects-only η to extrapolate. At n≥10 this lifts the cross-substrate Spearman ρ from +0.59 to **+0.97** (mid-term horizon, both substrates).
3. **Cross-check against a substrate-invariant physical metric** — mean future TEI, or fraction of cells where future TEI > 0.5. Both hit ρ ≥ 0.66 across the entire species set including small-N species.

See [`results/SUBSTRATE_SENSITIVITY_FINDINGS.md`](results/SUBSTRATE_SENSITIVITY_FINDINGS.md) for the full evidence — variant comparison tables at both horizons, decomposition of η into 10 GLMM terms per species, and refuted hypotheses.

## Quick start

```bash
git clone https://github.com/annefou/weatherxbiodiversity-substrate-sensitivity.git
cd weatherxbiodiversity-substrate-sensitivity
mamba env create -f environment.yml
mamba activate weatherxbiodiversity-substrate-sensitivity
snakemake --cores 1
```

This runs the four-step pipeline:

1. `notebooks/01_inputs_fetch.py` — fetches the upstream substrate artefacts. Two modes:
   - `MODE=local` (development) — symlinks from sibling working copies on the same filesystem.
   - `MODE=zenodo` — downloads from the upstream repos' Zenodo records (wired up after the upstream v0.1.0 releases are cut).
2. `notebooks/02_decompose.py` — per-species η decomposition diagnostic at the SSP3-7.0 mid-term horizon.
3. `notebooks/03_variants.py` — five-variant cross-substrate Spearman concordance at both horizons.
4. `notebooks/04_figures.py` — concordance heatmap + per-variant scatter pair-plots.

## What you get

- `results/SUBSTRATE_SENSITIVITY_FINDINGS.md` — the full findings document (mechanism, refuted hypotheses, scientific findings F1–F4 about Iberian *Bombus*, recommended reporting protocol).
- `results/variant_comparison_<horizon>.{csv,json}` — per-species per-variant rankings + Spearman concordance summaries.
- `results/substrate_comparison_decomposition_2030_2039.txt` — 12-species decomposition table.
- `figures/variant_concordance_<horizon>.png` — Spearman ρ heatmap (variant × n_cells filter).
- `figures/variant_pairs_<horizon>.png` — per-variant scatter, coloured by min(n_cells_64, n_cells_128).

## FORRT chain

This repo's FORRT chain is **paper-rooted on Soroye 2020** (the upstream paper whose TEI mechanism is being diagnosed). The CiTO citations reference both upstream replication chains:

- `extends` ↔ `weatherxbiodiversity-projection` FORRT chain
- `extends` ↔ `weatherxbiodiversity-projection-nside128` FORRT chain

Drafts live in [`nanopubs/drafts/`](nanopubs/drafts/). Published URIs go into [`nanopubs/PUBLISHED.md`](nanopubs/PUBLISHED.md).

## Citation

If you use this work, please cite:

- This software: [`CITATION.cff`](CITATION.cff) → DOI [10.5281/zenodo.20113786](https://doi.org/10.5281/zenodo.20113786)
- The original paper: [10.1126/science.aax8591](https://doi.org/10.1126/science.aax8591)
- The two upstream substrate replications via their own DOIs (see CITATION.cff `references`).

## Acknowledgements

Built from [`sciencelivehub/forrt-replication-template`](https://github.com/sciencelivehub/forrt-replication-template), part of the [Science Live platform](https://platform.sciencelive4all.org).
