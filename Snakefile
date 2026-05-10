# Snakefile — substrate-sensitivity diagnostic pipeline.
#
# This is a four-step methodological diagnostic that compares two upstream
# substrate replications (HEALPix nside=64 and nside=128) at the projection
# step. Inputs are fetched by 01_inputs_fetch.py — either symlinked from
# sibling local checkouts (development) or downloaded from upstream Zenodo
# records (release).
#
# Usage:
#   snakemake --cores 1                      # run everything
#   snakemake --cores 1 -n                   # dry run
#   INPUTS_FETCH_MODE=zenodo snakemake ...   # use Zenodo upstream artefacts

NOTEBOOKS = "notebooks"
INPUTS = "inputs"
RESULTS = "results"
FIGURES = "figures"

UPSTREAM_ARTEFACTS = expand(
    f"{INPUTS}/{{sub}}/posterior_vb_summary.csv",
    sub=("nside64", "nside128"),
)


rule all:
    input:
        f"{FIGURES}/variant_concordance_2030_2039.png",
        f"{FIGURES}/variant_pairs_2030_2039.png",
        f"{FIGURES}/variant_concordance_2020_2029.png",
        f"{FIGURES}/variant_pairs_2020_2029.png",
        f"{RESULTS}/variant_comparison_2030_2039.csv",
        f"{RESULTS}/variant_comparison_2020_2029.csv",
        f"{RESULTS}/substrate_comparison_decomposition_2030_2039.txt",


# ---------- 01: Fetch upstream substrate artefacts ----------
# Symlinks (MODE=local) or downloads (MODE=zenodo) the upstream substrate
# inputs into inputs/nside64/, inputs/nside128/, inputs/cea/.
rule inputs_fetch:
    output:
        UPSTREAM_ARTEFACTS,
        f"{INPUTS}/cea/dataGLMM_extinction.parquet",
    log:
        f"{RESULTS}/logs/01_inputs_fetch.log",
    shell:
        f"python {NOTEBOOKS}/01_inputs_fetch.py 2>&1 | tee {{log}}"


# ---------- 02: Per-species η decomposition diagnostic ----------
rule decompose:
    input:
        UPSTREAM_ARTEFACTS,
    output:
        f"{RESULTS}/substrate_comparison_decomposition_2030_2039.txt",
    shell:
        f"python {NOTEBOOKS}/02_decompose.py"


# ---------- 03: Five-variant cross-substrate concordance ----------
rule variants:
    input:
        UPSTREAM_ARTEFACTS,
        f"{INPUTS}/cea/dataGLMM_extinction.parquet",
    output:
        f"{RESULTS}/variant_comparison_2020_2029.csv",
        f"{RESULTS}/variant_comparison_2020_2029.json",
        f"{RESULTS}/variant_comparison_2030_2039.csv",
        f"{RESULTS}/variant_comparison_2030_2039.json",
    shell:
        f"python {NOTEBOOKS}/03_variants.py"


# ---------- 04: Figures ----------
rule figures:
    input:
        f"{RESULTS}/variant_comparison_2020_2029.json",
        f"{RESULTS}/variant_comparison_2030_2039.json",
    output:
        f"{FIGURES}/variant_concordance_2020_2029.png",
        f"{FIGURES}/variant_concordance_2030_2039.png",
        f"{FIGURES}/variant_pairs_2020_2029.png",
        f"{FIGURES}/variant_pairs_2030_2039.png",
    shell:
        f"python {NOTEBOOKS}/04_figures.py"
