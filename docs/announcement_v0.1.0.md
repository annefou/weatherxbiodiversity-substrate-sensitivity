# Launch announcement — v0.1.0 of the three-chain Iberian *Bombus* constellation

**Posting context:** LinkedIn, personal account (Anne Fouilloux). Bluesky version below is a 4-post thread.

**Headline figure:** `figures/projection_summary.png` (biodiversity hook). Optional second image: `figures/variant_concordance_2030_2039.png` (the methodological substrate-sensitivity heatmap — supports the "atomic claims enable this kind of cross-check" line in paragraph 3).

---

## LinkedIn — long-form post (~310 words)

What if the floor for "credible research" wasn't a paper, but a machine-readable chain of atomic, signed claims you could ask a database about — *did this mechanism replicate, on which substrates, with what numbers*?

The FAIR4RS community has made research software findable, accessible, interoperable, reusable. The Carpentries and CodeRefinery teach researchers how to write it. What's missing is the last step: the *claims that come out of the software* — also FAIR, also atomic, also citable. That's what FORRT nanopubs do. One claim per cryptographically-signed RDF document. Stand-alone, linked, composable.

We tested it on Soroye et al.'s (2020, *Science*) bumblebee-climate-change mechanism, applied to Iberian *Bombus* under SSP3-7.0 from Destination Earth's Climate Digital Twin. The thermal-niche exceedance coefficient replicates: β = +0.454, 95% HDI [+0.130, +0.751] at HEALPix nside=64, sign and order of magnitude matching the original — across three independent pixelisations on a region the original paper didn't fit. The mechanism holds. ✅

But here's where atomic claims actually pay off. The per-species *projection* ranking is grid-coupled below ~10 historical cells per substrate — the species the public most worries about (Pyrenean specialists, alpine *Bombus*) are precisely the ones this approach cannot reliably rank. That finding is its own nanopub — a separate Claim, a separate Outcome, *qualifying* the mechanism's projection-time use. Same paper, two distinct, machine-actionable claims about it.

🔗 Quote → AIDA → FORRT Claim → Replication Study → Replication Outcome → CiTO Citation + Research Software + Research Synthesis — 18 nanopubs, three Zenodo DOIs, three Jupyter Books:

https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/

If every species-distribution model paper published its substrate-sensitivity diagnostic this way, how much projection-replication consensus could we map?

#OpenScience #FAIR4RS #FORRT #biodiversity #DestinE

---

## Bluesky — 4-post thread (each post ≤ 300 chars)

**Post 1/4 (hook + figure):**
What if the floor for "credible research" wasn't a paper, but a machine-readable chain of atomic, signed claims you could ask a database about — *did this mechanism replicate, on which substrates, with what numbers*?

[attach figures/projection_summary.png]

**Post 2/4 (principle):**
FAIR4RS made research software FAIR. Carpentries and CodeRefinery teach how to write it. What's missing is the last step: the *claims that come out of the software* — also FAIR, also atomic, also citable. That's what FORRT nanopubs do.

**Post 3/4 (worked example):**
We tested it on Soroye et al. 2020 (*Science*) bumblebee-climate mechanism, applied to Iberian *Bombus* under DestinE Climate DT SSP3-7.0. β_TEI_delta = +0.454, HDI [+0.130, +0.751] at HEALPix nside=64. Replicates ✅ — across 3 substrates the original paper didn't fit.

**Post 4/4 (qualifier + close):**
But per-species *projection* ranking is grid-coupled below ~10 cells/substrate — Pyrenean alpine *Bombus* are exactly the species we can't rank reliably. That's its own atomic nanopub, *qualifying* the mechanism's projection use.

🔗 18 nanopubs, 3 Zenodo DOIs:
https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/

#OpenScience #FORRT

---

## Tips for posting

- **Personal account, not org account.** This is observation + advocacy, not platform marketing.
- **Don't tag Soroye / Newbold / Kerr.** Per DOMAIN.md — they'll find it via citation pipelines if it's notable.
- **Time it for Tuesday or Wednesday morning EU time.** Highest engagement window for science-policy LinkedIn.
- **Reply-to-yourself in the comments** with the other two repo URLs after posting — keeps the main post tight, the comment thread becomes the artefact index.
- **Engage with replies in the first 90 minutes.** Algorithms reward early reply density.

## What's deliberately NOT in the post

- The specific top-3 high-risk species (*B. humilis*, *B. muscorum*, *B. ruderarius*). Naming them invites disagreement on biological details and distracts from the meta-claim about atomic publishing. The Jupyter Book has them.
- The 30% substrate-robustness margin (we say "within ±30%" implicitly via "+0.454" near the original). Numbers fight for attention; one is enough.
- The full URI of every nanopub. We let the constellation graph live in the Jupyter Book.
- A self-congratulatory closing. The closing is a question, not a victory lap.

## Variants for other accounts

If a Science Live or FAIR4RS org account picks this up, the org-account variant should:
- Open with "Three FORRT chains went live this week …" (rather than the personal hook).
- Embed the variant_concordance heatmap as the lead figure (org accounts can afford the heavier methodological framing).
- Closing question reframed: "Which species-distribution model paper would benefit most from this kind of multi-substrate FORRT diagnostic?"
