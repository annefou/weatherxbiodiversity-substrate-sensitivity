# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
# ---

# %% [markdown]
# # 01 — Fetch upstream substrate inputs
#
# This repo is a methodological diagnostic that compares per-species
# extirpation-risk projections across two upstream substrate replications:
#
# - **HEALPix nside=64** — `annefou/weatherxbiodiversity-projection`
# - **HEALPix nside=128** — `annefou/weatherxbiodiversity-projection-nside128`
#
# Both upstream repos must have a v0.1.0 (or later) GitHub release whose
# Zenodo deposit contains the artefacts listed below. This notebook fetches
# them into `inputs/nside64/` and `inputs/nside128/`, plus the CEA reference
# scaling file from the nside=64 repo into `inputs/cea/`.
#
# **Required artefacts per substrate (relative paths within the upstream repo):**
#
# - `healpix_port/outputs_iberia/posterior_vb_summary.csv`
# - `healpix_port/outputs_iberia/dataGLMM_extinction.parquet`
# - `healpix_port/outputs_iberia/climate_tei_pei_healpix.nc`
# - `healpix_port/outputs_iberia/sampling_continent_healpix.nc`
# - `healpix_port/outputs_iberia/presence_absence_healpix.nc`
# - `healpix_port/outputs_iberia/climate_tei_pei_future_2020_2029_healpix.nc`
# - `healpix_port/outputs_iberia/climate_tei_pei_future_2030_2039_healpix.nc`
# - `results/posterior_bambi_healpix.nc`
#
# **CEA reference scaling (nside=64 repo only):**
#
# - `soroye_port/outputs_iberia/dataGLMM_extinction.parquet`
#
# ## Two modes
#
# 1. **Zenodo (released)** — set `MODE = "zenodo"`. Requires the upstream
#    Zenodo concept DOIs. Filled in once the upstream releases are cut.
# 2. **Local development** — set `MODE = "local"`. Symlinks the artefacts
#    from sibling working copies on the filesystem.

# %%
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# %% [markdown]
# ## Configuration

# %%
MODE = os.environ.get("INPUTS_FETCH_MODE", "local")

# Local development paths — used when MODE == "local"
LOCAL_NSIDE64 = Path(
    os.environ.get(
        "LOCAL_NSIDE64",
        Path.home() / "Documents/ScienceLive/weatherxbiodiversity-projection",
    )
)
LOCAL_NSIDE128 = Path(
    os.environ.get(
        "LOCAL_NSIDE128",
        Path.home() / "Documents/ScienceLive/weatherxbiodiversity-projection-nside128",
    )
)

# Zenodo concept-record IDs (v0.1.0 releases cut 2026-05-10).
#
# Concept DOIs (always resolve to the latest version):
#   nside=64:  https://doi.org/10.5281/zenodo.20113777
#   nside=128: https://doi.org/10.5281/zenodo.20113780
#
# The MODE='zenodo' fetch path is not yet wired (would require downloading
# the Zenodo source tarball and extracting specific files). MODE='local'
# remains the default and recommended dev path. Filling these in here so
# a future v0.2.0 implementation has the IDs ready.
ZENODO_NSIDE64_RECORD: str | None = "20113777"
ZENODO_NSIDE128_RECORD: str | None = "20113780"

ARTEFACTS_HEALPIX = [
    "healpix_port/outputs_iberia/posterior_vb_summary.csv",
    "healpix_port/outputs_iberia/dataGLMM_extinction.parquet",
    "healpix_port/outputs_iberia/climate_tei_pei_healpix.nc",
    "healpix_port/outputs_iberia/sampling_continent_healpix.nc",
    "healpix_port/outputs_iberia/presence_absence_healpix.nc",
    "healpix_port/outputs_iberia/climate_tei_pei_future_2020_2029_healpix.nc",
    "healpix_port/outputs_iberia/climate_tei_pei_future_2030_2039_healpix.nc",
    "results/posterior_bambi_healpix.nc",
]
ARTEFACT_CEA = "soroye_port/outputs_iberia/dataGLMM_extinction.parquet"


# %%
def link_local(src: Path, dst: Path) -> None:
    """Symlink src into dst, creating dst's parents and overwriting any prior link."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.is_symlink() or dst.exists():
        dst.unlink()
    dst.symlink_to(src.resolve())


def fetch_local(label: str, upstream_root: Path, target: Path, paths: list[str]) -> None:
    print(f"\n[{label}] symlinking from {upstream_root}")
    for rel in paths:
        src = upstream_root / rel
        dst = target / Path(rel).name
        if not src.exists():
            raise SystemExit(
                f"  MISSING: {src} — has the upstream pipeline been run?"
            )
        link_local(src, dst)
        print(f"  {dst.name}  <-  {src}")


def fetch_zenodo(label: str, record_id: str, target: Path, paths: list[str]) -> None:
    raise SystemExit(
        f"[{label}] Zenodo fetch not yet wired — upstream v0.1.0 release pending. "
        f"Use MODE='local' until then."
    )


# %%
if MODE == "local":
    fetch_local("nside=64", LOCAL_NSIDE64, REPO_ROOT / "inputs" / "nside64", ARTEFACTS_HEALPIX)
    fetch_local("nside=128", LOCAL_NSIDE128, REPO_ROOT / "inputs" / "nside128", ARTEFACTS_HEALPIX)
    fetch_local("CEA", LOCAL_NSIDE64, REPO_ROOT / "inputs" / "cea", [ARTEFACT_CEA])
elif MODE == "zenodo":
    if not (ZENODO_NSIDE64_RECORD and ZENODO_NSIDE128_RECORD):
        raise SystemExit(
            "ZENODO_NSIDE64_RECORD / ZENODO_NSIDE128_RECORD not yet set. "
            "Cut upstream v0.1.0 releases first, then update this notebook."
        )
    fetch_zenodo("nside=64", ZENODO_NSIDE64_RECORD, REPO_ROOT / "inputs" / "nside64", ARTEFACTS_HEALPIX)
    fetch_zenodo("nside=128", ZENODO_NSIDE128_RECORD, REPO_ROOT / "inputs" / "nside128", ARTEFACTS_HEALPIX)
    fetch_zenodo("CEA", ZENODO_NSIDE64_RECORD, REPO_ROOT / "inputs" / "cea", [ARTEFACT_CEA])
else:
    raise SystemExit(f"Unknown MODE={MODE!r}; use 'local' or 'zenodo'.")
