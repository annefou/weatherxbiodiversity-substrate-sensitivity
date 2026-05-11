# 06 — CiTO Citation

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Description:** *"Declare citations between papers or other works, using Citation Typing Ontology"*

## Field-by-field draft

### Identifier for the citing creative work (text input, required)

URI of the Outcome published in step 05. Pull from `nanopubs/PUBLISHED.md`.

```
<replace-with-published-Outcome-URI-from-step-05>
```

### List citations (repeatable group, required ≥1)

#### Citation 1 — back to the original paper (Soroye 2020)

##### Citation Type (dropdown)

- [x] **`qualifies`**

(Outcome verdict is PartiallySupported, which maps to CiTO `qualifies`. The TEI mechanism Soroye et al. introduced REPLICATES at fit time across three substrates — the qualification is downstream, about how to USE the fitted GLMM at the projection step. This is not a refutation; it is a methodological caveat that extends the mechanism's applicability conditions.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.1126/science.aax8591
```

#### Citation 2 — extends the canonical nside=64 sibling chain

##### Citation Type (dropdown)

- [x] **`extends`**

(This Study takes the canonical nside=64 replication's outputs as input artefacts and produces a methodological diagnostic that complements its Outcome. The nside=64 sibling's Outcome reports per-species rankings filtered per the recommended protocol from THIS chain.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.5281/zenodo.20113777
```

(Concept DOI of `weatherxbiodiversity-projection`. Or, once published, paste the canonical nside=64 sibling Outcome URI directly.)

#### Citation 3 — extends the nside=128 substrate-extension sibling chain

##### Citation Type (dropdown)

- [x] **`extends`**

(Likewise, this Study takes the nside=128 substrate-extension's outputs as input artefacts. The nside=128 sibling's Outcome also reports rankings filtered per the recommended protocol from this chain.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.5281/zenodo.20113780
```

(Concept DOI of `weatherxbiodiversity-projection-nside128`.)

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 06.

This completes the six-step FORRT chain. Optional next layers:

- **Research Software** (`drafts/07_research_software.md`) — if the repo *produces* a reusable software artefact.
- **Research Synthesis** (`drafts/08_synthesis.md`) — if this chain is one of several testing facets of a shared property.
