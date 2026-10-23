import streamlit as st
from ui.components import inject_css, hero, section, footer

st.set_page_config(page_title="Resources — KCB", page_icon="📚", layout="wide")
inject_css()
hero()

section("📚 Resources")

st.markdown("### Data sources")
st.markdown(
    """
- **USGS sediment-hosted copper deposits** — [ScienceBase](https://www.usgs.gov/)
- **USGS Northwest Botswana Rift tract** — `sedCu_tracts` layer
- **USGS Africa Mineral GIS** — mineral facilities, roads, rail
- **Khoemacau** — [Mindat](https://www.mindat.org/)
- **Motheo** — [Sandfire Resources](https://www.sandfire.com.au/)
"""
)

section(" Further reading")
st.markdown(
    """
- Kalahari Copper Belt geology and DKF-NPF contact models — _background only, not used in the current ranking_
- Sediment-hosted copper deposit classification (USGS)
- Streamlit + Folium deployment patterns for geospatial decision-support
"""
)

section("Built with")
st.markdown(
    """
- **Streamlit** — web interface
- **Folium** — interactive mapping
- **Pandas** — shortlist handling
- **GeoJSON** — spatial context
- **USGS public data** — inputs
"""
)

footer()