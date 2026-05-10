# 05 — FORRT Replication Outcome

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify the actual numerical results first** by reading `results/SUBSTRATE_SENSITIVITY_FINDINGS.md` and `scripts/compare_variants.py`. Don't quote numbers from memory. See `docs/verify-before-drafting.md`.

## Field-by-field draft

### Short URI suffix for outcome ID (text input, required)

```
soroye2020-tei-projection-substrate-coupling-partially-supported
```

### Plain-text label for the outcome (text input, required)

```
TEI-based extirpation projection is grid-coupled at the projection step (Iberian Bombus, HEALPix nside=64 vs nside=128, SSP3-7.0): mechanism replicates at fit time, per-species ranking does not — fixable
```

### Search for a FORRT replication study (search/select, required)

URI of the Replication Study published in step 04 of THIS chain. Pull from `nanopubs/PUBLISHED.md` after step 04 is live.

```
<replace-with-published-Study-URI-from-step-04>
```

### Repository URL (text input, required)

```
https://github.com/annefou/weatherxbiodiversity-substrate-sensitivity
```

### Completion date (date picker, required)

```
2026-05-10
```

### Validation status (dropdown, required)

- [ ] Validated
- [x] **PartiallySupported**
- [ ] Contradicted

Maps to CiTO `qualifies` in step 06. The TEI mechanism Soroye et al. (2020) introduced is REPLICATED at fit time — sc_TEI_delta is positive, large, and credible at three independent spatial substrates within ±30%. The per-species PROJECTION under SSP3-7.0 is grid-coupled at the projection step, with per-species η swinging 1–9 logits between nside=64 and nside=128 for species observed in fewer than ~10 historical cells. The mechanism is supported; its application to per-species future projection is qualified.

### Confidence level (dropdown, required)

```
High
```

(Findings cross-validated against two upstream substrate replications, two horizons, five projection variants, and four cell-count filters; mechanistic decomposition isolates the substrate-coupling source to within a single GLMM term.)

### Describe the overall conclusion about the original claim (textarea, required)

```
This methodological diagnostic compares two single-substrate replications of Soroye et al. (2020) for Iberian Bombus under DestinE Climate DT SSP3-7.0 — at HEALPix nside=64 (~92 km, weatherxbiodiversity-projection) and nside=128 (~46 km, weatherxbiodiversity-projection-nside128). Both upstream Outcomes confirm Soroye's TEI mechanism is substrate-robust at fit time (sc_TEI_delta within ±30% across three substrates including the original CEA grid).

Headline finding: per-species ranking under SSP3-7.0 IS grid-coupled at the projection step. The same physical climate signal at the same Iberian location produces per-species η swings of 1–9 logits between nside=64 and nside=128 for species observed in fewer than ~10 historical cells.

The substrate-coupling is not caused by per-species random-effect refit (substrate-stable, ΔRE ≤ 0.6 logits across all species), nor by per-species niche-limit refit (modest, ΔT_range = 0–3°C; species with identical T_range still show 8.8-logit projection swings). It is caused by two mechanisms acting together:

(i) Per-species sample size at projection time. Below ~10 occupied + active cells per substrate, per-cell extrapolation noise dominates the species-mean η regardless of which projection variant is used.

(ii) The GLMM interaction term sc_TEI_delta:sc_PEI_delta — the largest single contributor to projection η at SSP3-7.0 — compounds substrate-specific predictor standardisation quadratically when future predictors extrapolate 2–4σ outside the training distribution. The same physical climate signal z-scores to opposite tails of the standardised distribution under each substrate's local (μ, σ); the interaction term scales as the product, amplifying the divergence.

These two mechanisms are diagnosable, mechanistic, and fixable. Three principled fixes are validated empirically:

(a) Per-species cell-count filter. Restricting reporting to species with at least 10 occupied + active cells per substrate brings cross-substrate Spearman ρ from +0.27 (full GLMM, all species) to +0.59 at the same variant, +0.97 at variant (b) below.

(b) Drop the GLMM interaction terms at projection time only. Keep them in the fit (they are part of Soroye's specification) but do NOT use them to extrapolate. At n≥10 + main-effects-only η, cross-substrate Spearman ρ = +0.97 (mid-term horizon) — near-perfect agreement.

(c) Cross-check against substrate-invariant physical metrics. Mean future TEI per species and fraction of cells where future TEI exceeds 0.5 are physically grounded and substrate-invariant in physical units; ρ ≥ +0.66 at all sample sizes (better than any GLMM-based variant for low-N species).

Refuted hypothesis: re-standardising future predictors against a shared CEA reference (without refitting β) does NOT decouple the substrate. The GLMM β coefficients are fit against substrate-local σ; just rescaling the predictors at projection time is mathematically equivalent to a constant scale shift and does not change the ranking. Properly testing this fix requires refitting the GLMM with shared standardisation (out of scope here).

The mechanism IS substrate-robust at fit time. Its per-species PROJECTION at the species-cell level is qualified — reliable above the n_cells filter, not below it. Both upstream Outcomes report rankings filtered per the recommended protocol from this chain.
```

### Describe the evidence that supports your conclusion (textarea, required)

```
Five projection variants tested at both horizons (2020–2029 + 2030–2039) and four per-species n_cells filters (≥1, ≥5, ≥10, ≥20) on 31 Iberian Bombus species shared between the two upstream substrate replications.

Variants:
  (a) Full GLMM η, within-substrate predictor standardisation.
  (b) Main-effects-only η, within-substrate standardisation (drop the four interaction terms at projection only; keep them in the fit).
  (c) Full GLMM η, shared CEA reference standardisation (substrate-fit β + shared (μ, σ); refuted as a standalone fix).
  (d) Mean future TEI per species (substrate-invariant physical metric, no GLMM).
  (d2) Fraction of cells with future TEI > 0.5 per species (substrate-invariant threshold metric).

Cross-substrate Spearman ρ between nside=64 and nside=128 rankings, mid-term horizon 2030–2039:

                                  n≥1  n≥5  n≥10  n≥20
                                  (31) (27) (13)  (10)
  (a) Full GLMM η                 +0.27 +0.51 +0.59 +0.77
  (b) Main-effects only η         +0.40 +0.52 +0.97 +0.98
  (c) Shared CEA reference η      +0.27 +0.49 +0.52 +0.55
  (d) Mean future TEI             +0.66 +0.69 +0.90 +0.82
  (d2) Frac TEI_future>0.5        +0.66 +0.71 +0.88 +0.83

Headline: variant (b) at n≥10 lifts ρ from +0.59 (variant a same filter) to +0.97 — substrate-stable. Same qualitative pattern at the near-term horizon.

Mechanistic decomposition. Per-species η at the SSP3-7.0 mid-term horizon was decomposed into its 10 GLMM-term contributions plus the species random intercept, at both substrates. For the four most-divergent species (norvegicus, mendax, jonellus, sylvestris):

  - sc_TEI_delta:sc_PEI_delta term contributions differ by 1.0–6.3 logits between substrates (largest single driver in every case).
  - sc_TEI_delta term contributions differ by 0.5–2.5 logits (next largest).
  - All other terms (Intercept, sc_sampling, main TEI/PEI, all other interactions, species RE) differ by ≤ 0.6 logits each (substrate-stable).

Refuted hypotheses verified empirically:
  - Random-intercept refit. ΔRE across all 12 species in the diagnostic set ≤ 0.6 logits — substrate-stable.
  - Niche-limit refit. ΔT_range across the 12 species = 0.0–2.9°C; norvegicus has ΔT_range = +0.01°C yet shows 8.8-logit Δη — refuted as the dominant cause.
  - Shared-reference standardisation alone. Variant (c) Spearman ρ stays ≈ variant (a) at every cell-count filter.

Files: results/SUBSTRATE_SENSITIVITY_FINDINGS.md, results/variant_comparison_2030_2039.{csv,json}, results/variant_comparison_2020_2029.{csv,json}, results/substrate_comparison_decomposition_2030_2039.txt, figures/variant_concordance_{2020_2029,2030_2039}.png, figures/variant_pairs_{2020_2029,2030_2039}.png.
```

### Describe what limits the conclusions of the study (textarea, optional)

```
1. Two substrates only. The diagnostic compares nside=64 and nside=128 (both HEALPix-NESTED on the WGS84 ellipsoid). Whether the same recommended protocol holds at coarser substrates (nside=32, nside=16) or against non-HEALPix grids (CEA, EASE-Grid 2.0, S2) is not directly tested. The within-HEALPix factor-of-2 resolution change is the strongest case where one might expect substrate stability; finding instability here is a strong negative result, but the empirical n_cells ≥ 10 threshold may be substrate-pair-dependent.

2. Variant (c) tested as approximation of refit-with-shared-standardisation. The most rigorous test of "shared reference standardisation alone fixes substrate coupling" is to refit the GLMM with shared (μ, σ) and re-project. This Outcome instead uses substrate-local β with shared-σ predictors at projection time, which is mathematically equivalent to a constant scaling — refuting it as a standalone fix BUT not the same as testing a full refit. A full refit could be a follow-up.

3. Iberian Bombus only. The diagnostic uses the species set, climate inputs (CRU TS 3.24.01), and projection (DestinE Climate DT SSP3-7.0) from the upstream replications. Whether the substrate-coupling mechanism generalises to other taxa, regions, or future climate forcings is plausible from the mechanism (it depends only on having an interaction-term GLMM with future predictors extrapolating outside the training distribution) but is not directly tested.

4. Recommended protocol bound to this analysis. The "n_cells ≥ 10 + main-effects-only η" recommendation is calibrated against the empirical Spearman ρ at the two horizons tested. Other choices may be defensible (e.g. n ≥ 5 + variant b also gives ρ = +0.52; n ≥ 20 + variant a gives ρ = +0.77). The protocol is a recommendation, not a hard threshold.

5. Validation status PartiallySupported, not Contradicted. Soroye's TEI mechanism IS supported at fit time (the upstream chains' Outcomes are Validated). The qualification is downstream — about how to USE the fitted GLMM at projection time. CiTO step 06 should encode this as cito:qualifies (extends with a methodological caveat) rather than cito:disputes (refutes).
```

> **Drafter notes — additional context for finalising this Outcome.**
>
> - This Outcome anchors a **methodological** claim derived from two single-substrate replication chains. CiTO step 06 should `cito:qualifies` Soroye 2020 (the original paper, with the projection-time methodological caveat) AND `cito:extends` BOTH upstream replication chains (the canonical nside=64 sibling and the nside=128 substrate-extension sibling).
> - The recommended protocol — "n_cells ≥ 10 per substrate + main-effects-only η at projection time" — is the load-bearing methodological recommendation. Both upstream Outcomes already report their rankings filtered per this protocol.

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 05.
