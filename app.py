import streamlit as st
from streamlit_folium import st_folium
from services.loader import load_shortlist, load_geojson
from services.ranker import filter_by_posture
from services.report import to_csv_bytes
from ui.components import (
    inject_css, hero, section,
    metric_cards, shortlist_table, build_map, footer,
)

st.set_page_config(
    page_title="KCB Copper Target Screening",
    page_icon="💎",
    layout="wide",
)

inject_css()
hero()

df = load_shortlist()
tract = load_geojson("kcb_tract.geojson")
anchors = load_geojson("anchors.geojson")

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    posture = st.radio(
        "Ranking posture",
        ["Consensus only", "Conservative", "Default", "Exploratory"],
        help="Conservative weights infrastructure proximity. Exploratory weights known-copper proximity.",
    )
    st.markdown("---")
    st.markdown(
        "**Legend**\n\n"
        "🔴 Consensus target\n\n"
        "🔵 Selected target\n\n"
        "⚫ Other candidates\n\n"
        "🏭 Anchor mine"
    )

view, rank_col = filter_by_posture(df, posture)

# Section 1: metrics
section(" 1. Shortlist at a glance")
metric_cards(view, df)

# Section 2: table + download
section(f" 2. Ranked targets — {posture}")
shortlist_table(view)

st.download_button(
    "⬇️ Download filtered CSV",
    to_csv_bytes(view),
    file_name=f"shortlist_{posture.lower().replace(' ', '_')}.csv",
    mime="text/csv",
)

# Section 3: map
section(" 3. Target locations")
m = build_map(df, view, tract, anchors)
st_folium(m, width=None, height=560)

footer()