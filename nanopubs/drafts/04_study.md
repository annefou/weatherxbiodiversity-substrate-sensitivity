# 04 — FORRT Replication Study

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify code first:** read the actual reproduction script in `notebooks/03_analysis.py` before writing the methodology field. See `docs/verify-before-drafting.md`.

## Field-by-field draft

### Short URI suffix for study ID (text input, required)

Slug. Use kebab-case.

```
soroye2020-tei-projection-substrate-sensitivity-cross-substrate-diagnostic
```

### Label/name of replication study (text input, required)

Human-readable title.

```
Cross-substrate substrate-sensitivity diagnostic for TEI-based extirpation projection (Iberian Bombus, HEALPix nside=64 vs nside=128, SSP3-7.0)
```

### Study type (dropdown, required)

- [ ] Reproduction Study — direct reproduction: same methodology, same tools.
- [x] **Replication Study** — replication with different methodology or conditions.
- [ ] Reproduction/Replication Study — both.

This is a methodological diagnostic Study that compares two prior single-substrate replications. The "different methodology" is the cross-substrate variant comparison + per-species η decomposition, which neither upstream chain performs.

### Search for a FORRT claim (search/select, required)

URI of the Claim published in step 03. Pull from `nanopubs/PUBLISHED.md`.

```
<replace-with-published-Claim-URI-from-step-03>
```

### Describe what part of the claim is reproduced/replicated (textarea, required)

The **scope** of the claim being tested. Which aspect, what's in/out of scope. NOT methodology. NOT results. See `docs/pico-study-outcome-levels.md`.

```
SCOPE: the cross-substrate concordance of per-species ranking from Soroye et al. 2020's TEI-based GLMM, when projected to SSP3-7.0 future climate from two single-substrate Iberian Bombus replications.

IN SCOPE
  - The TWO substrates that the upstream replications already published as GitHub releases + Zenodo deposits: HEALPix nside=64 (~92 km, weatherxbiodiversity-projection v0.1.0) and HEALPix nside=128 (~46 km, weatherxbiodiversity-projection-nside128 v0.1.0).
  - The TWO horizons that DestinE Climate DT SSP3-7.0 has populated: 2020–2029 and 2030–2039.
  - FIVE projection variants (full GLMM η, main-effects-only η, shared-CEA-reference η, mean future TEI, fraction TEI_future > 0.5).
  - FOUR per-species n_cells filters (≥1, ≥5, ≥10, ≥20).
  - Mechanistic decomposition of per-species η into 10 GLMM-term contributions plus the species random intercept, at both substrates, for a diagnostic set of 12 species spanning the n_cells distribution.

OUT OF SCOPE
  - Other substrates (CEA, EASE-Grid 2.0, S2, additional HEALPix levels) — flagged in the Outcome's Limitations.
  - Other species or regions — Iberian Bombus only.
  - Other future climate forcings — SSP3-7.0 only.
  - End-of-century horizons (2046–2055, 2076–2085) — DestinE Climate DT archive unavailable past 2039 at time of analysis.
```

### Describe how the claim is reproduced/replicated (textarea, required)

The **method** in plain prose. Read `notebooks/03_analysis.py` and any config files first. NOT exact numerical results.

```
METHOD

The diagnostic reads input artefacts from two upstream substrate replications (the canonical nside=64 sibling and the nside=128 substrate-extension sibling) and computes five candidate per-species rankings at each substrate, plus a mechanistic per-species η decomposition.

Inputs (per substrate; symlinked from sibling repos in development, fetched from Zenodo in v0.2.0):
  - GLMM coefficient posterior (variational-Bayes summary): healpix_port/outputs_iberia/posterior_vb_summary.csv
  - Species random intercepts (full NUTS posterior): results/posterior_bambi_healpix.nc
  - Substrate-local predictor scaling (μ, σ): healpix_port/outputs_iberia/dataGLMM_extinction.parquet
  - Per-species niche limits T_min_spp, T_max_spp, P_min_spp, P_max_spp: healpix_port/outputs_iberia/climate_tei_pei_healpix.nc
  - Future-period predictors (per species per cell): climate_tei_pei_future_<horizon>_healpix.nc
  - Per-species observation mask: presence_absence_healpix.nc
  - Per-cell sampling effort: sampling_continent_healpix.nc

Five projection variants (notebooks/02_decompose.py and 03_variants.py):
  (a) Full GLMM η, within-substrate predictor standardisation.
  (b) Main-effects-only η, within-substrate standardisation (drop the four interaction terms at projection only; keep them in the fit).
  (c) Full GLMM η, shared CEA reference standardisation (substrate-fit β + shared (μ, σ) computed from the original Soroye CEA pool; tested as a refit-equivalent approximation).
  (d) Mean future TEI per species (substrate-invariant physical metric, no GLMM).
  (d2) Fraction of cells with future TEI > 0.5 per species (substrate-invariant threshold metric).

For each variant, compute per-species community-mean η (or fraction) across the species' currently-occupied + active cells, at both substrates and both horizons. Apply four n_cells filters (≥1, ≥5, ≥10, ≥20). Compute Spearman rank correlation between nside=64 and nside=128 rankings under each (variant, filter) combination.

Mechanistic decomposition (scripts/compare_substrates.py): for a diagnostic set of 12 species spanning the n_cells distribution, decompose per-species η into its 10 GLMM-term contributions plus the species random intercept at each substrate. Identify which term(s) are responsible for substrate-coupling.

Code: scripts/compare_substrates.py, scripts/compare_variants.py, scripts/plot_variant_concordance.py. Notebooks: 01_inputs_fetch.py, 02_decompose.py, 03_variants.py, 04_figures.py.
```

### Describe any deviations from original methodology (textarea, optional)

What's different from the original method. Verify against the actual code, don't guess.

```
1. Different methodological character. Soroye et al. 2020 fit one GLMM at the CEA grid and reported a continental-scale extirpation summary. This Study does NOT refit the GLMM — it uses the substrate-fit GLMMs from the two upstream replications and asks how their per-species PROJECTION rankings concord across substrates. The substrate-coupling diagnostic is downstream of Soroye's mechanism, not a direct replication of it.

2. Variant (c) tested as approximation. The most rigorous test of "shared reference standardisation alone fixes substrate coupling" is to refit the GLMM with shared (μ, σ) and re-project. Variant (c) here uses substrate-local β with shared-σ predictors at projection time — mathematically equivalent to a constant scaling of η, refuting the hypothesis as a standalone fix BUT not the same as testing a full refit. Documented in the Outcome's Limitations as a deferred follow-up.

3. Substrate-invariant physical metrics added. Variants (d) and (d2) compute per-species mean future TEI and fraction TEI_future>0.5 — physical-unit metrics that bypass the GLMM entirely. These are NOT in Soroye's original analysis; they are introduced here as a substrate-invariant cross-check.
```

### Search keywords (Wikidata) (multi-select, optional)

Provide labels (not QIDs) — the Wikidata search picks up labels.

- bumblebee
- climate change
- generalized linear mixed model
- HEALPix
- species distribution model
- methodology
- replication study

### Search discipline (Wikidata) (search, optional)

Provide labels.

- macroecology
- biogeography
- methodology
- statistics

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 04.
