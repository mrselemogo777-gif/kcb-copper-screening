import streamlit as st
import folium
from folium.plugins import Fullscreen, MiniMap

def inject_css():
    st.markdown(
        """
        <style>
        .block-container { padding-top: 2rem; max-width: 1200px; }
        .kcb-hero {
            background: linear-gradient(135deg, #fde68a 0%, #f59e0b 100%);
            padding: 1.6rem 2rem; border-radius: 14px; margin-bottom: 1.5rem;
        }
        .kcb-hero h1 { margin: 0; color: #1f2937; font-size: 2.1rem; }
        .kcb-hero p  { margin: 0.4rem 0 0; color: #374151; font-size: 1.02rem; }
        .kcb-scope {
            background: #fef3c7; border-left: 6px solid #d97706;
            padding: 1rem 1.2rem; border-radius: 8px; margin-bottom: 1.5rem;
            color: #78350f; font-size: 0.96rem;
        }
        .kcb-section {
            font-size: 1.25rem; font-weight: 700; color: #1f2937;
            margin: 1.8rem 0 0.6rem; padding-bottom: 0.3rem;
            border-bottom: 2px solid #fde68a;
        }
        .kcb-metric {
            background: #fffbeb; border: 1px solid #fde68a;
            border-radius: 10px; padding: 1rem; text-align: center;
        }
        .kcb-metric .v { font-size: 1.7rem; font-weight: 800; color: #b45309; }
        .kcb-metric .l { font-size: 0.82rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.04em; }
        .kcb-footer {
            margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e5e7eb;
            font-size: 0.82rem; color: #6b7280; text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def hero():
    st.markdown(
        """
        <div class="kcb-hero">
            <h1>💎 KCB Copper Target Screening</h1>
            <p>Sediment-hosted copper · Kalahari Copper Belt · USGS Northwest Botswana Rift tract · 2 consensus targets</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def scope_banner():
    st.markdown(
        """
        <div class="kcb-scope">
        <b> Decision-support tool, not a discovery prediction.</b>
        All ranked targets must be confirmed by a qualified geologist before any
        data-acquisition or drilling decision. Does not incorporate EICB proprietary
        data or drill-hole assays.
        </div>
        """,
        unsafe_allow_html=True,
    )

def section(title: str):
    st.markdown(f'<div class="kcb-section">{title}</div>', unsafe_allow_html=True)

def metric_cards(view, full):
    c1, c2, c3, c4 = st.columns(4)
    vals = [
        ("Targets shown", len(view)),
        ("Consensus targets", int((full["label"] == "Consensus").sum())),
        ("Mean anchor dist.", f"{view['dist_anchor_km'].mean():.1f} km"),
        ("Mean known-Cu dist.", f"{view['dist_known_cu_km'].mean():.1f} km"),
    ]
    for col, (label, value) in zip((c1, c2, c3, c4), vals):
        col.markdown(
            f'<div class="kcb-metric"><div class="v">{value}</div>'
            f'<div class="l">{label}</div></div>',
            unsafe_allow_html=True,
        )

def shortlist_table(view):
    st.dataframe(
        view[["label", "lat", "lon", "dist_anchor_km", "dist_known_cu_km", "dist_road_km"]]
            .round(2)
            .rename(columns={
                "label": "Tier", "lat": "Lat", "lon": "Lon",
                "dist_anchor_km": "→ Anchor (km)",
                "dist_known_cu_km": "→ Known Cu (km)",
                "dist_road_km": "→ Road (km)",
            }),
        use_container_width=True,
        hide_index=True,
    )

def build_map(full, view, tract, anchors):
    m = folium.Map(location=[-21.5, 24.0], zoom_start=6, tiles="CartoDB positron")
    Fullscreen().add_to(m)
    MiniMap(toggle_display=True).add_to(m)

    if tract:
        folium.GeoJson(
            tract,
            style_function=lambda _: {
                "fillColor": "#fde68a", "color": "#b45309",
                "weight": 2, "fillOpacity": 0.25,
            },
            name="KCB tract",
        ).add_to(m)

    if anchors:
        for feat in anchors["features"]:
            lon, lat = feat["geometry"]["coordinates"]
            folium.Marker(
                location=[lat, lon],
                icon=folium.Icon(color="darkblue", icon="industry", prefix="fa"),
                popup=feat["properties"].get("name", "Anchor"),
                tooltip=feat["properties"].get("name", "Anchor"),
            ).add_to(m)

    keep = set(zip(view["lat"].round(6), view["lon"].round(6)))
    for _, row in full.iterrows():
        kept = (round(row["lat"], 6), round(row["lon"], 6)) in keep
        colour = "#b91c1c" if row["label"] == "Consensus" else ("#1d4ed8" if kept else "#9ca3af")
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=9 if kept else 5,
            color=colour,
            weight=2 if kept else 1,
            fill=True,
            fill_color=colour,
            fill_opacity=0.9 if kept else 0.3,
            popup=(
                f"<b>{row['label']}</b><br>"
                f"Anchor {row['dist_anchor_km']:.1f} km<br>"
                f"Known Cu {row['dist_known_cu_km']:.1f} km<br>"
                f"Road {row['dist_road_km']:.1f} km"
            ),
        ).add_to(m)

    folium.LayerControl(collapsed=True).add_to(m)
    return m

def footer():
    st.markdown(
        '<div class="kcb-footer">KCB Copper Target Screening · EICB × MDO · '
        'Public USGS data · MIT License · Author: Legakwa Selemogo</div>',
        unsafe_allow_html=True,
    )
