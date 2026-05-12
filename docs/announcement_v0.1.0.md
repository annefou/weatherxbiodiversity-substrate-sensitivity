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

---

## Variant 2 — methodology / FORRT audience, constellation graph as hero

Post this **about one week after Variant 1**. Variant 1 brings the biodiversity audience; Variant 2 brings the Open Science / FORRT / nanopub / FAIR4RS audience. The two posts share infrastructure (same Jupyter Book URLs, same Zenodo DOIs) but lead with very different framings.

**Hero figure:** the constellation graph from `https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/nanopubs/published`. To get a PNG of the rendered mermaid diagram:

```bash
# Option A — screenshot the deployed page (easiest)
# Open the URL above, scroll to the "Constellation graph" heading, screenshot the rendered mermaid.

# Option B — render the mermaid source to SVG/PNG with mermaid-cli
npm install -g @mermaid-js/mermaid-cli
mmdc -i nanopubs/PUBLISHED.md -o constellation.png -t default -b transparent
```

LinkedIn renders PNG > SVG > GIF for image previews; export at 1500×1500 px or larger for high-DPI screens.

### LinkedIn — long-form post (~320 words)

Eighteen cryptographically signed RDF documents — that's the entire provenance trail of a multi-substrate climate-biodiversity replication. Three FORRT chains, sharing the Quote, AIDA, and Claim at the abstract layer, branching at the methodology layer, converging at a Research Synthesis at the apex. Everything machine-actionable.

When we publish a paper, the "what was tested, where it held, where it didn't" lives in the prose — not searchable, not composable, not citable as separate claims. FORRT nanopubs invert that. Every empirical claim a paper makes can become a separate, atomic, cryptographically-signed RDF document on the nanopub network, with CiTO citations linking back to the source paper and to sibling claims.

We tested it on Soroye et al. (2020, *Science*) bumblebee–climate mechanism, replicated on Iberian *Bombus* at three independent spatial substrates (CEA, HEALPix nside=64, nside=128) plus a cross-substrate diagnostic. The Quote — Soroye's verbatim sentence — is one URI shared across all three chains. The AIDA + Claim layer is shared between the two replication chains and separate for the methodological diagnostic. Studies, Outcomes, and CiTO Citations branch per substrate. One Research Synthesis at the top pulls all three Outcomes together.

Here's why this shape matters: anyone asking the nanopub network *"what's the substrate-robustness evidence for Soroye's TEI mechanism?"* gets three Outcomes from one query. Anyone asking *"where does this mechanism break down at projection time?"* gets the `qualifies` citation from the substrate-sensitivity chain. The constellation IS the answer — you don't have to read three papers + a discussion section + a supplementary table to find out.

🔗 The full graph, all 18 URIs, three Jupyter Books:
https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/nanopubs/published

What's the smallest research artefact you wish were a separately citable claim today?

#OpenScience #FAIR4RS #FORRT #nanopub #knowledgegraph

### Bluesky — 4-post thread (each post ≤ 300 chars)

**Post 1/4 (hook + constellation image):**
Eighteen cryptographically signed RDF docs = the entire provenance trail of a multi-substrate climate-biodiversity replication. Three FORRT chains, sharing the abstract layer, branching at methodology, converging at a Synthesis. Everything machine-actionable.

[attach constellation graph PNG]

**Post 2/4 (principle):**
A paper's "what was tested, where it held, where it didn't" lives in prose — not searchable, not composable. FORRT nanopubs invert that. Every empirical claim becomes a separate, atomic, signed RDF document, with CiTO citations linking back to source + siblings.

**Post 3/4 (worked example):**
Tested on Soroye 2020's bumblebee-climate mechanism, replicated on Iberian Bombus at three substrates (CEA + HEALPix nside=64 + nside=128) + a cross-substrate diagnostic. Quote, AIDA, Claim shared across chains; Studies and Outcomes branch per substrate; one Synthesis at the apex.

**Post 4/4 (close):**
Ask the nanopub network "what's the substrate-robustness evidence?" → 3 Outcomes from 1 query. Ask "where does it break?" → the qualifies citation. The constellation IS the answer.

🔗 https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/nanopubs/published

#OpenScience #FORRT #nanopub

### How Variant 2 differs from Variant 1

| Aspect | Variant 1 (biology) | Variant 2 (methodology) |
|---|---|---|
| Hero image | `projection_summary.png` (species + map) | Constellation graph (18-node mermaid) |
| Lead | "credible research as machine-readable chains" | "18 RDF docs = entire provenance trail" |
| Worked example | The biology result (+0.454, top-3 species) | The constellation shape (shared layer → branches → synthesis) |
| Closing question | About species-distribution-model replication consensus | About what the smallest separately-citable artefact should be |
| Hashtags | `#biodiversity #DestinE` | `#nanopub #knowledgegraph` |
| Audience | Biodiversity / climate / EU funding | Open Science / FORRT / nanopub / library + RDM |

### Timing rationale

Posting both variants on consecutive days saturates the same algorithmic window. Spacing them ~1 week apart:
- Variant 1's engagement plateau (~5 days) is over before Variant 2 launches.
- Variant 2 reaches people who didn't engage with the biology framing but DO engage with FORRT / FAIR4RS framing.
- Cross-post-2-to-post-1 in a reply comment after Variant 2 goes live ("for the worked biology details, see [link to Variant 1]") — turns the two posts into a coherent thread for anyone who finds either one.
