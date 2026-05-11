# 03 — FORRT Claim

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Form heading:** *"FORRT Claim — Declare an original claim according to FORRT, linking it to an AIDA sentence with a specific FORRT type."*

## Field-by-field draft

### Short URI suffix as claim ID (text input, required)

Slug becomes part of the nanopub URI. Use kebab-case.

```
soroye2020-tei-projection-grid-coupled-low-n
```

### Label of the claim (text input, required)

A descriptive title (not a sentence). Used for searches/discovery.

```
TEI-based extirpation projection per-species ranking is grid-coupled at the projection step for low-N species
```

### Search for an AIDA sentence (search/select, required)

URI of the AIDA published in step 02. Pull from `nanopubs/PUBLISHED.md`.

> _If the AIDA was published via Nanodash (`w3id.org/np/...` namespace), the platform's search may not find it — paste the URI manually._

```
<replace-with-published-AIDA-URI-from-step-02>
```

### Type of FORRT claim (dropdown, required)

Pick one. See `docs/claim-type-vocabulary.md` for the seven options and how to choose.

- [ ] computational performance
- [ ] scalability
- [ ] data quality
- [ ] data governance
- [ ] descriptive pattern
- [x] **model performance**
- [ ] statistical significance

The claim is about the GLMM's behaviour at projection time (its predictive ranking is substrate-coupled when extrapolating outside the training distribution for species with few observations). This is canonically a "model performance" FORRT claim — about how reliably the model generalises — rather than "statistical significance" (which would be about a coefficient's posterior credibility, the topic of the upstream replication chains' Claims).

### Source URI (text input, optional)

Full URL form: `https://doi.org/...` (NOT bare DOI).

```
https://doi.org/10.1126/science.aax8591
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 03.
