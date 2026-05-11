# 01 — Quote-with-comment (paper-rooted chains)

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> If this is a question-rooted chain, use `01_pico.md` or `01_pcc.md` instead — see `docs/chain-decision-tree.md`.

**Form heading:** *"Annotate a paper quotation — Annotating a paper quotation with personal interpretation"*

## Field-by-field draft

### Cited DOI (text input)

Format: starts with `10.` — bare DOI, **NOT** `https://doi.org/...` form.

```
10.1126/science.aax8591
```

### Quote mode (radio button)

- [x] **Quote whole text (less than 500 characters)**
- [ ] Quote start/end *(use this if the quote exceeds 500 chars)*

### Quoted Text (textarea, required)

Verbatim from the paper PDF in `paper/`. Character-for-character. ≤ 500 chars in whole-text mode.

Source: Soroye, Newbold, Kerr (2020), *Science* 367(6478): 685, **Abstract** (p. 685, second-to-last sentence of the abstract paragraph).

```
Increasing frequency of hotter temperatures predicts species' local extinction risk, chances of colonizing a new area, and changing species richness.
```

Character count: 149 / 500.

### Comment (textarea, required)

Subtitle: *"Our interpretation or explanation of why this quotation is relevant."*

Why this quote matters and what the replication tests. Connect the paper's claim to the work this repo does. Don't repeat the quote.

```
This sentence states the mechanism — frequency of temperatures exceeding species' historical thermal tolerances drives local extinction, colonization, and richness change — whose forward-projection behaviour this methodological diagnostic interrogates. The original paper validated this mechanism retrospectively for 66 Bombus species across North America and Europe at ~50 km / monthly resolution. Two upstream Iberian replications (weatherxbiodiversity-projection at HEALPix nside=64 and weatherxbiodiversity-projection-nside128) confirm the mechanism replicates at fit time across three substrates within ±30%. This study asks: when the same fitted GLMM is used to project to SSP3-7.0 future climate, does the per-species extirpation-risk ranking depend on the spatial pixelisation? The answer (yes, for species observed in fewer than ten historical cells) qualifies — but does NOT refute — the original mechanism. We anchor on this sentence because the diagnostic is downstream of the mechanism it characterises, not a refutation of it.
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 01.
