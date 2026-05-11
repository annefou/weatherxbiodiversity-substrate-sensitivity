# 08 — Research Synthesis (optional)

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> Use this template only when this chain is **one of several** testing facets of a shared underlying property. The Synthesis names the cross-cutting conclusion and lists the multiple Outcomes as supporting sources.

**Form heading:** *"Science Live Research Synthesis — Synthesise findings across multiple replication outcomes with conclusions, recommendations, conditions, and limitations."*

## Field-by-field draft

### Short URI suffix for synthesis ID (text input, required)

Slug. Use kebab-case.

```
soroye2020-tei-mechanism-replicates-at-fit-but-projection-is-grid-coupled
```

### Label of the synthesis (text input, required)

A one-line summary.

```
Soroye et al. 2020's TEI-based extirpation mechanism is substrate-robust at fit time but grid-coupled at projection time for low-N species; here is the diagnostic and the recommended reporting protocol
```

### Conclusion of the synthesis (textarea, required)

The aggregate finding across the underlying outcomes.

```
Synthesising the three sibling FORRT chains on Iberian Bombus (canonical CEA + HEALPix nside=64 replication, HEALPix nside=128 substrate extension, and this cross-substrate diagnostic), Soroye et al.'s (2020) TEI-based extirpation mechanism resolves into two empirically distinct claims:

(A) At fit time the mechanism IS substrate-robust on Iberian Bombus. The GLMM coefficient on standardised TEI_delta is positive and credibly above zero at three independent pixelisations (CEA +0.479; HEALPix nside=64 +0.454; HEALPix nside=128 +0.347), with all three estimates within ±30 percent. Soroye's central biological claim REPLICATES.

(B) At projection time the per-species ranking is NOT substrate-robust below ~10 occupied + active cells per substrate. Per-species community-mean η differs by 1 to 9 logits between nside=64 and nside=128 under DestinE Climate DT SSP3-7.0 for the 18 of 31 species below the cell-count threshold, including narrowly-distributed Pyrenean specialists (B. pyrenaeus, B. mucidus, B. mendax). The substrate-coupling is mechanistically diagnosable: the GLMM interaction term sc_TEI_delta:sc_PEI_delta compounds substrate-specific predictor standardisation quadratically when future predictors extrapolate 2–4σ outside the training distribution.

These two claims are not in tension — they describe different parts of the modelling pipeline. The original mechanism is sound; the projection-time application is qualified. Three principled fixes are empirically validated: (i) per-species cell-count filter at n_cells ≥ 10; (ii) drop the GLMM interaction terms at projection time only; (iii) cross-check against substrate-invariant physical metrics (mean future TEI, fraction TEI_future > 0.5). At n ≥ 10 with main-effects-only η, cross-substrate Spearman ρ = +0.97 (mid-term horizon) — substrate-stable.
```

### Recommendations (textarea, required)

Actionable guidance for practitioners.

```
1. When replicating Soroye-style TEI extirpation models, expect substrate-robust headline coefficients within ±30% across factor-of-2 HEALPix resolution changes — substrate sensitivity at FIT time is small. Cite multiple substrates jointly when claiming substrate-robustness; a single substrate is not sufficient evidence.

2. When projecting to future climate, ALWAYS filter per-species reporting to species with at least 10 occupied + active cells per substrate. Below this, per-species ranking is grid-coupled and not interpretable.

3. At projection time, drop the GLMM interaction terms from the linear predictor used for extrapolation. Keep them in the FIT (they are part of Soroye's specification) but use main-effects-only η to project. This single change lifts cross-substrate Spearman ρ from +0.59 (full GLMM) to +0.97 at n ≥ 10.

4. Cross-check ANY GLMM-based ranking against the substrate-invariant physical metric "mean future TEI per species" or "fraction of cells with TEI_future > 0.5". If the GLMM main-effects ranking and the physical ranking disagree for a given species, the GLMM is unreliable for that species at that substrate.

5. CiTO encoding: cito:confirms for the fit-time substrate-robustness; cito:qualifies for projection-time use without the recommended protocol; cito:extends to this diagnostic when reporting projection results at a new substrate pair.

6. The recommended protocol is empirically calibrated against HEALPix nside=64 vs nside=128 for Iberian Bombus on DestinE Climate DT SSP3-7.0. Different taxon/region/forcing combinations may require different thresholds; the protocol is a recommendation, not a hard constraint.
```

### Conditions under which the synthesis applies (textarea, required)

Scope: data types, methods, domains, regions, time periods.

```
- Region: Iberian peninsula (the three synthesised chains all use Iberian Bombus only).
- Species set: Bombus species observed in GBIF on the Iberian peninsula in 1901–2014 (31 species in the joint analysis).
- Climate forcing for fit: CRU TS 3.24.01 monthly temperature and precipitation, identical to Soroye et al. 2020 (Figshare deposit).
- Climate forcing for projection: DestinE Climate DT SSP3-7.0, IFS-NEMO standard, native HEALPix nside=128. Horizons 2020–2029 and 2030–2039 only (DestinE archive populated through 2039 at time of analysis).
- Spatial substrates analysed: CEA (~100 km), HEALPix-NESTED nside=64 (~92 km), HEALPix-NESTED nside=128 (~46 km) on the WGS84 ellipsoid.
- GLMM specification: Soroye et al. 2020's full formula with main effects + four predictor interaction terms + per-species random intercept.
- Inference: full-posterior NUTS via bambi/PyMC; HDIs reported.
- This synthesis covers BOTH the fit-time substrate-robustness AND the projection-time grid-coupling — these are the two complementary aspects of the same three-chain constellation.
```

### Limitations of the synthesis (textarea, required)

What was not tested? What might not generalise?

```
1. Three substrates only (CEA, HEALPix nside=64, HEALPix nside=128). Whether the same fit-time substrate-robustness AND projection-time grid-coupling pattern hold at coarser substrates (nside=32 or 16) or against non-HEALPix grids was not directly tested.

2. One region (Iberian peninsula). High-latitude or alpine Bombus systems may behave differently — niche margins, sampling effort, and per-species cell counts all differ.

3. One climate dataset for FIT (CRU TS 3.24.01) and one for PROJECTION (DestinE Climate DT SSP3-7.0, IFS-NEMO standard). Multi-model ensemble robustness and reanalysis-substitution robustness are not addressed.

4. The recommended n_cells ≥ 10 threshold is empirically calibrated on this specific analysis. Whether 10 generalises is open. Below the threshold the per-species ranking is grid-coupled; above it, the recommended protocol yields ρ_Spearman = +0.97 across substrates — but the empirical threshold may be different for taxa with different occupancy distributions.

5. Variant (c) "shared CEA reference standardisation" was tested as an approximation of refit-with-shared-standardisation, not as a true refit. The most rigorous test of "is standardisation reference choice alone sufficient" is to refit the GLMM with shared (μ, σ) and re-project — a deferred follow-up.

6. Time horizon. SSP3-7.0 mid-term (2030–2039) is the strongest test horizon currently available. End-of-century horizons (2046–2055, 2076–2085) are deferred until the DestinE Climate DT archive extends past 2050.

7. The synthesis treats the mechanism's projection-time grid-coupling as a methodological caveat, not a refutation of Soroye et al.'s biological claim. This framing assumes the user accepts the mechanism's epistemic separation between FIT (substrate-robust) and PROJECTION (qualified).
```

### Completion date (date picker, required)

```
2026-05-11
```

### Supporting sources (repeatable group, required ≥1)

Each entry is a URL — typically the FORRT Outcome URIs being synthesised. Pull from `nanopubs/PUBLISHED.md` (and/or registries from sibling repos).

- This chain's Outcome (step 05): `<replace-with-published-Outcome-URI-from-step-05>`
- Sibling canonical nside=64 chain's Outcome: `<replace-with-nside64-sibling-Outcome-URI>` (or, before publication: https://doi.org/10.5281/zenodo.20113777)
- Sibling nside=128 substrate-extension chain's Outcome: `<replace-with-nside128-sibling-Outcome-URI>` (or, before publication: https://doi.org/10.5281/zenodo.20113780)
- This repo's Research Software nanopub (step 07 of this chain): `<replace-with-published-Research-Software-URI-from-step-07>`
- Soroye, Newbold & Kerr (2020): https://doi.org/10.1126/science.aax8591

### Search topics (Wikidata) (multi-select, optional)

Provide labels (not QIDs).

- bumblebee
- climate change
- species distribution model
- generalized linear mixed model
- HEALPix
- methodology
- replication
- DestinE Climate DT
- Iberian Peninsula

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 08.
