# 02 — AIDA Sentence

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Form heading:** *"AIDA Sentence — Make structured scientific claims following the AIDA model"*

## Field-by-field draft

### AIDA sentence (textarea, required)

Atomic, Independent, Declarative, Absolute. One empirical finding. Must end with a full stop.

> _If your draft AIDA contains "and" linking two distinct findings, split into two AIDA nanopubs._

```
Per-species ranking of Iberian Bombus extirpation risk under DestinE Climate DT SSP3-7.0, computed from the GLMM linear predictor at the projection step using Soroye et al. 2020's TEI mechanism, is sensitive to the spatial pixelisation: per-species community-mean log-odds-of-extirpation differs by 1 to 9 logits between HEALPix-NESTED nside=64 and nside=128 for species observed in fewer than ten historical Iberian cells per substrate.
```

### Select related topics/tags (dropdown, optional)

Predefined topic vocabulary — list the labels you intend to pick from the dropdown.

```
biodiversity
climate change
species distribution modelling
methodology
replication
```

### Relates to this nanopublication (text input, required)

URI of the nanopub the AIDA derives from.

- For paper-rooted chains: the Quote-with-comment URI (from step 01).
- For question-rooted chains: the PICO or PCC URI (from step 01).

Pull the URI from `nanopubs/PUBLISHED.md`.

```
<replace-with-published-Quote-URI-from-step-01>
```

### Supported by datasets (repeatable group, optional)

DOIs/URLs of datasets that ground the AIDA claim.

- This repo's Zenodo concept DOI: `10.5281/zenodo.20113786`
- The canonical nside=64 sibling repo's Zenodo concept DOI: `10.5281/zenodo.20113777`
- The nside=128 substrate-extension sibling's Zenodo concept DOI: `10.5281/zenodo.20113780`

### Supported by other publications (repeatable group, optional)

DOIs/URLs of publications that support the AIDA claim — e.g. peer-reviewed methods papers, or the original paper if not already cited via the Quote.

- 10.1126/science.aax8591 (Soroye, Newbold & Kerr 2020 — original paper introducing the TEI mechanism whose projection-step substrate-coupling this AIDA characterises)

> **Known platform bug (2026-04-26):** if both *Supported by datasets* AND *Supported by other publications* are populated and publishing fails, fall back to publishing this AIDA via Nanodash. The URI namespace becomes `https://w3id.org/np/...` (still valid and citable).

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 02.
