import streamlit as st
from ui.components import inject_css, hero, section, footer

st.set_page_config(page_title="About — KCB", page_icon="ℹ️", layout="wide")
inject_css()
hero()

section("📚 Data sources")
st.markdown(
    """
- **USGS sediment-hosted copper deposits** — `sedCu_deps_pros`
- **USGS Northwest Botswana Rift tract** — `sedCu_tracts`
- **USGS Africa Mineral GIS** — mineral facilities, roads, rail
- **Anchor coordinates** — Khoemacau (Mindat), Motheo (Sandfire/Mapcarta)
"""
)

section(" Method")
st.markdown(
    """
1. Build a 25 km candidate grid inside the KCB tract → **211 candidates**.
2. Compute three proximity features: distance to anchor mines, distance to known
   sediment-hosted copper, distance to major roads.
3. Normalize each and combine under three weightings:
   - **Conservative** — 0.7 anchor + 0.3 known Cu (infrastructure-led)
   - **Default** — 0.5 anchor + 0.5 known Cu (balanced)
   - **Exploratory** — 0.3 anchor + 0.7 known Cu (geology-led)
4. **Consensus** = intersection of the top-5 under all three postures → **2 targets**.

_The ranking is proximity-based only. It does not model DKF-NPF contact geometry,
stratigraphic traps, or mineral-system fertility._
"""
)

section(" Independent checks")
st.markdown(
    """
| Check | Result |
|---|---|
| KMeans vs ranking (ARI) | **0.099** — clusters separate by distance magnitude, not rank tier |
| Monte Carlo top-3 stability | **100%** across 100 runs |
| Monte Carlo top-7–10 stability | **<20%** — treat as review shortlist |
"""
)

footer()