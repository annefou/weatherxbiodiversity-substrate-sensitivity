# Published FORRT nanopublication constellation

This chapter is the canonical cross-chain view of the three-repository constellation. Every nanopub URI links to the [Science Live platform](https://platform.sciencelive4all.org) viewer (replace `<URI>` in `https://platform.sciencelive4all.org/np/?uri=<URI>` if a direct link doesn't open).

## What is in the constellation

Three FORRT chains, derived from Soroye et al. 2020 ([10.1126/science.aax8591](https://doi.org/10.1126/science.aax8591)) — the same upstream paper anchors all three. The three chains test complementary claims:

- **`weatherxbiodiversity-projection`** (Zenodo: [10.5281/zenodo.20113777](https://doi.org/10.5281/zenodo.20113777)) — replicates Soroye's TEI-based extirpation mechanism on Iberian *Bombus* at the original CEA grid + HEALPix nside=64. **Outcome: Validated** → CiTO `confirms` Soroye 2020.
- **`weatherxbiodiversity-projection-nside128`** (Zenodo: [10.5281/zenodo.20113780](https://doi.org/10.5281/zenodo.20113780)) — same mechanism, refit at HEALPix nside=128 (DestinE Climate DT native pixelisation). **Outcome: Validated** → CiTO `confirms` Soroye 2020 + `extends` the nside=64 sibling.
- **`weatherxbiodiversity-substrate-sensitivity`** *(this repository)* (Zenodo: [10.5281/zenodo.20113786](https://doi.org/10.5281/zenodo.20113786)) — methodological diagnostic showing that the same fitted GLMM, when projected to SSP3-7.0, has grid-coupled per-species rankings for low-N species. **Outcome: PartiallySupported** → CiTO `qualifies` Soroye 2020 + `extends` both upstream chains.

Eighteen unique nanopubs in total. The Quote (Soroye's verbatim sentence) is shared across all three chains; the AIDA + Claim for the mechanism finding are shared across the two replication chains; the substrate-sensitivity chain has its own AIDA + Claim about the methodological finding; each chain has its own Study, Outcome, CiTO Citation, and Research Software nanopub; one Research Synthesis at the apex pulls all three Outcomes together.

## Constellation graph

```{mermaid}
graph TB
    Soroye(["Soroye et al. 2020<br/>10.1126/science.aax8591"]):::paper

    Quote(["01 — Quote<br/>RAErLL…"]):::shared

    AIDA_mech(["02 — AIDA: TEI_delta positive<br/>RAgb6p…"]):::shared
    Claim_mech(["03 — Claim: statistical significance<br/>RAh7NY…"]):::shared

    AIDA_substr(["02 — AIDA: projection grid-coupled<br/>RAwGAt…"]):::ss
    Claim_substr(["03 — Claim: model performance<br/>RAVfoa3…"]):::ss

    Study_64(["04 — Study: CEA + nside=64<br/>RAybO8c8…"]):::nside64
    Outcome_64(["05 — Outcome: Validated<br/>RAPZMgc…"]):::nside64
    CiTO_64(["06 — CiTO: confirms<br/>RALbHA-…"]):::nside64
    RS_64(["07 — Research Software<br/>RAKH9X…"]):::nside64

    Study_128(["04 — Study: nside=128 refit<br/>RAsGeFqq…"]):::nside128
    Outcome_128(["05 — Outcome: Validated<br/>RAa4QR41…"]):::nside128
    CiTO_128(["06 — CiTO: confirms<br/>RAhw9m0B…"]):::nside128
    RS_128(["07 — Research Software<br/>RA-GY81…"]):::nside128

    Study_ss(["04 — Study: cross-substrate<br/>RAPZ97EG…"]):::ss
    Outcome_ss(["05 — Outcome: PartiallySupported<br/>RAD19jy…"]):::ss
    CiTO_ss(["06 — CiTO: qualifies<br/>RAumfa30…"]):::ss
    RS_ss(["07 — Research Software<br/>RAfdV1y…"]):::ss

    Synth(["08 — Research Synthesis<br/>RA5TJV…"]):::apex

    Soroye --> Quote
    Quote --> AIDA_mech
    Quote --> AIDA_substr
    AIDA_mech --> Claim_mech
    AIDA_substr --> Claim_substr

    Claim_mech --> Study_64
    Claim_mech --> Study_128
    Claim_mech -.-> RS_64
    Claim_mech -.-> RS_128
    Claim_substr --> Study_ss
    Claim_substr -.-> RS_ss

    Study_64 --> Outcome_64 --> CiTO_64
    Study_128 --> Outcome_128 --> CiTO_128
    Study_ss --> Outcome_ss --> CiTO_ss

    Outcome_64 --> Synth
    Outcome_128 --> Synth
    Outcome_ss --> Synth

    classDef paper fill:#fff3b0,stroke:#7a5901,stroke-width:2px,color:#000
    classDef shared fill:#e8e8e8,stroke:#444,color:#000
    classDef nside64 fill:#cfe8fc,stroke:#0072B2,color:#000
    classDef nside128 fill:#d6f5d6,stroke:#1a9850,color:#000
    classDef ss fill:#fde0d4,stroke:#D55E00,color:#000
    classDef apex fill:#e6cffd,stroke:#6a3d9a,stroke-width:2px,color:#000
```

**Reading the graph:** solid arrows are chain-derivation links (each step references the URI of the previous step's nanopub); dotted arrows are the optional Research Software back-links to the FORRT Claim. The Synthesis at the apex pulls in all three Outcomes as `supporting sources`. CiTO Citation cross-references (each chain's CiTO `extends` the other chains' Outcomes) are not drawn — they would clutter; see each CiTO nanopub for its citation list.

## Per-chain URI registry

### Chain 1 — `weatherxbiodiversity-projection` (canonical Iberian *Bombus* replication)

| Step | Template | URI |
|---|---|---|
| 01 | Quote-with-comment | <https://w3id.org/sciencelive/np/RAErLL_QSe3e0pKBxHkUHH5v49F66fFVuS2OmYMJz02OY> |
| 02 | AIDA Sentence — TEI_delta positive on Iberian *Bombus* | <https://w3id.org/sciencelive/np/RAgb6pxwyANh-jpPdiY3H5k-fGWGgCmN72UrV_zAJcSMI> |
| 03 | FORRT Claim — statistical significance | <https://w3id.org/sciencelive/np/RAh7NYjme8dajwxnoBfbOjsd1L76LQfN-pMEajIwiRDJE> |
| 04 | Replication Study — CEA + HEALPix nside=64 | <https://w3id.org/sciencelive/np/RAybO8c8qx0p5bz9lMhMxzNsXhp0aXyd8GHnGC3i53vQY> |
| 05 | Replication Outcome — **Validated** | <https://w3id.org/sciencelive/np/RAPZMgcYbScSAXnrnSySQwZzgSA_rn-xodlMxNlwwQYY8> |
| 06 | CiTO Citation — `confirms` Soroye 2020 | <https://w3id.org/sciencelive/np/RALbHA-r6wIFOFPFlfIpwYqJEpzCFqeJ082iChgdfvhNM> |
| 07 | Research Software | <https://w3id.org/sciencelive/np/RAKH9XeZn3CUr9WaFKMC3O2pT_HJJ96c3jTa6v6dWEE3c> |

### Chain 2 — `weatherxbiodiversity-projection-nside128` (substrate extension)

| Step | Template | URI |
|---|---|---|
| 01 | Quote — *shared with Chain 1* | <https://w3id.org/sciencelive/np/RAErLL_QSe3e0pKBxHkUHH5v49F66fFVuS2OmYMJz02OY> |
| 02 | AIDA — *shared with Chain 1* | <https://w3id.org/sciencelive/np/RAgb6pxwyANh-jpPdiY3H5k-fGWGgCmN72UrV_zAJcSMI> |
| 03 | FORRT Claim — *shared with Chain 1* | <https://w3id.org/sciencelive/np/RAh7NYjme8dajwxnoBfbOjsd1L76LQfN-pMEajIwiRDJE> |
| 04 | Replication Study — HEALPix nside=128 refit | <https://w3id.org/sciencelive/np/RAsGeFqqv4iQqrFNyjQwpSqKQYYk8JqGEjpCCJf1FtAM4> |
| 05 | Replication Outcome — **Validated** | <https://w3id.org/sciencelive/np/RAa4QR41Hot9zxujcrCyTo82Ij7oaw_6z8zk8NxDqoJFM> |
| 06 | CiTO Citation — `confirms` + `extends` | <https://w3id.org/sciencelive/np/RAhw9m0BEj0-9hXrTtJ2NHG5rMr-ZBf_mdBQTQRk6u3n4> |
| 07 | Research Software | <https://w3id.org/sciencelive/np/RA-GY814xxcpEsUWozEJKHGG39bDV8gkbor7OhX8QpVPE> |

### Chain 3 — `weatherxbiodiversity-substrate-sensitivity` (this repository, methodological diagnostic)

| Step | Template | URI |
|---|---|---|
| 01 | Quote — *shared with Chains 1+2* | <https://w3id.org/sciencelive/np/RAErLL_QSe3e0pKBxHkUHH5v49F66fFVuS2OmYMJz02OY> |
| 02 | AIDA — projection grid-coupled for low-N species | <https://w3id.org/sciencelive/np/RAwGAtWnn1ghSvSzTUtTfrKN4PZP7W6OBmdYsfVRjWAx8> |
| 03 | FORRT Claim — model performance | <https://w3id.org/sciencelive/np/RAVfoa34PLT_3LhfcWLBZ9BQHs43euvrwaTyO9mgk-QcQ> |
| 04 | Replication Study — cross-substrate diagnostic | <https://w3id.org/sciencelive/np/RAPZ97EGTne_ZhBh_WE1_QX1Jgf96DWlNg-jsgasx5g50> |
| 05 | Replication Outcome — **PartiallySupported** | <https://w3id.org/sciencelive/np/RAD19jydIHgfVpRQiA8mqvVUefOd7FFwA4tLIfkXmOJmc> |
| 06 | CiTO Citation — `qualifies` + `extends` | <https://w3id.org/sciencelive/np/RAumfa30WMPlQksc1f6XdslPtXS2z4-_3DCZC3ln57PKc> |
| 07 | Research Software — diagnostic toolkit | <https://w3id.org/sciencelive/np/RAfdV1yB1JksVJ7dJYwECRHVMhNzbGcjUAa6UreqG_fM4> |
| 08 | **Research Synthesis** | <https://w3id.org/sciencelive/np/RA5TJVZ0_5Knzxd4OtOoZgO6ZspWHwVCSLWNNd7V9H6QQ> |

## How to view a nanopub

Open any URI directly in your browser. Science Live's viewer renders the four named graphs (Head, Assertion, Provenance, PublicationInfo) of each nanopub. If a direct link doesn't resolve (some networks block the redirect), wrap the URI in the viewer URL:

```
https://platform.sciencelive4all.org/np/?uri=<full-URI>
```

## Format notes

- URIs from Science Live are of the form `https://w3id.org/sciencelive/np/RA…`. URIs from Nanodash (used as a fallback when the Science Live UI hits a bug) are of the form `https://w3id.org/np/RA…`. Both are valid and citable.
- The trailing `…` in the diagram are visual truncations; the URIs above are full.
- Nanopubs are **immutable** once published. To correct a published nanopub, publish a retraction or supersession nanopub (see `docs/programmatic-nanopubs.md`).
