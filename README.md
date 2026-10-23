# KCB Copper Target Screening 

Decision-support tool that ranks candidate copper target areas inside the USGS Northwest Botswana Rift tract (Kalahari Copper Belt), using proximity to existing operations and known sediment-hosted copper occurrences.

##  Scope

Prioritization aid, not a prediction of discovery. All ranked targets must be confirmed by a qualified geologist before any data-acquisition or drilling decision. Does not incorporate EICB proprietary data or drill-hole assays.

##  Ranking Output

| Metric | Value |
|---|---|
| Candidate targets inside KCB tract | 211 |
| Consensus targets (top-5 in all three postures) | 2 |
| Anchor mines used | 2 (Khoemacau, Motheo) |
| Known sediment-hosted Cu deposits inside tract | 2 (Ngwako Pan, Ghanzi) |

Consensus coordinates:

| Latitude | Longitude | Dist. to anchor | Dist. to known Cu |
|---|---|---|---|
| −20.929 | 22.81 | 25.2 km | 36.1 km |
| −20.926 | 23.05 | 46.2 km | 20.2 km |

##  Independent Checks

| Check | Result |
|---|---|
| KMeans vs ranking (ARI) | 0.099 — clusters separate by distance magnitude, not rank tier |
| Monte Carlo top-3 stability | 100% across 100 runs |
| Monte Carlo top-7–10 stability | <20% — treat as review shortlist |

## 🖥️ Features

- Target Screening page with three operating points (Conservative / Default / Exploratory)
- Consensus-only filter
- Filtered table with coordinates and distances
- Interactive map with KCB tract, anchor mines, and ranked targets
- Downloadable filtered CSV
- 3 demo postures for instant testing

##  Tech Stack

- Streamlit web interface
- Pandas for shortlist handling
- Folium for interactive mapping
- GeoJSON for spatial context
- USGS Africa Mineral GIS + USGS sediment-hosted copper database
- Anchor coordinates: Khoemacau (Mindat), Motheo (Sandfire/Mapcarta)

## 📦 Installation

```bash
git clone https://github.com/mrselemogo777-gif/kcb-copper-screening.git
cd kcb-copper-screening
pip install -r requirements.txt
streamlit run app.py
