import streamlit as st
from ui.components import inject_css, hero, section, footer

st.set_page_config(page_title="Help — KCB", page_icon="📖", layout="wide")
inject_css()
hero()

section(" What this app does")
st.markdown(
    """
This app is a **viewer** for a copper target screening already completed in a Jupyter notebook.
It does **not** re-run the analysis, re-rank targets, or pull live data. It loads a pre-computed
shortlist of candidate target areas inside the USGS Northwest Botswana Rift tract (Kalahari
Copper Belt) and lets you filter, inspect, map, and download that shortlist.

The ranking is based on **proximity only**:

- Distance to the two nearest anchor mines (Khoemacau, Motheo)
- Distance to the two known sediment-hosted copper deposits inside the tract (Ngwako Pan, Ghanzi)
- Distance to major roads (used only for the held-out validation, not the main ranking)

It does **not** model DKF-NPF contact geometry, stratigraphic traps, or mineral-system fertility.
"""
)

section("🧭 How to use it")
st.markdown(
    """
**1. Pick a posture in the sidebar.**

| Posture | What it weights | When to use |
|---|---|---|
| **Consensus only** | Shows only the 2 targets that rank top-5 under all three weightings | The shortest possible shortlist — the two targets the method is most confident about |
| **Conservative** | 0.7 anchor + 0.3 known Cu | When infrastructure proximity matters most (roads, power, existing operations) |
| **Default** | 0.5 anchor + 0.5 known Cu | Balanced view — the recommended starting point |
| **Exploratory** | 0.3 anchor + 0.7 known Cu | When known-copper proximity matters more than infrastructure |

**2. Read the metric cards.** They show how many targets are in the current view, how many are
consensus, and the mean distance to anchors and to known copper for the visible set.

**3. Read the table.** Each row is one candidate target with its latitude, longitude, tier label
(Consensus / Anchor-only / Copper-only), and the three distances. Distances are in kilometres.

**4. Use the map.** Red dots are consensus targets, blue dots are targets in the current posture,
grey dots are other candidates. Blue triangles are the two anchor mines. The amber outline is the
KCB tract. Click any marker for its distances.

**5. Download if you need it.** The **Download filtered CSV** button exports the current view —
useful for bringing the shortlist into a GIS or a report.
"""
)

section(" What the targets mean")
st.markdown(
    """
Each target is a **25 km grid cell** inside the KCB tract that was scored by proximity to
anchors and known copper. It is a *prioritization aid*, not a drill target. A target that
scores well means: *this cell is close to existing operations and close to known copper —
it deserves a closer look by a geologist.*

**The two consensus targets** are the ones that survive all three weightings:

| Latitude | Longitude | → Anchor | → Known Cu |
|---|---|---|---|
| −20.929 | 22.81 | 25.2 km | 36.1 km |
| −20.926 | 23.05 | 46.2 km | 20.2 km |

Both sit near the Ngwako Pan deposit (−20.75, 23.10), which is the geographic plausibility check.
"""
)

section(" How confident is the ranking")
st.markdown(
    """
Three independent checks were run in the notebook:

| Check | Result | What it tells you |
|---|---|---|
| KMeans vs ranking (ARI) | **0.099** | Clusters separate by distance magnitude, not by rank tier — the ranking is not just recovering one cluster |
| Monte Carlo top-3 stability | **100%** across 100 runs | The top three targets are stable to anchor ±3 km and copper ±15% perturbation |
| Monte Carlo top-7–10 stability | **<20%** | Targets below rank 6 are a review list, not a shortlist |

In plain terms: **the top three are robust. The rest are worth a look but not a commitment.**
"""
)

section(" What this app does not do")
st.markdown(
    """
- It does not predict discovery. The ranking is a prioritization aid.
- It does not model geology — no DKF-NPF contact, no stratigraphy, no mineral-system fertility.
- It does not update live. The shortlist is fixed; re-run the notebook to change it.
- It does not replace a geologist. Every target requires field confirmation.
"""
)

section(" For developers")
st.markdown(
    """
- **Data source:** `outputs/shortlist.csv` (the ranking) and three GeoJSON files (tract, anchors, targets).
- **To re-run the ranking:** open the notebook, re-execute, re-export the four files, refresh the app.
- **To change weights:** edit the notebook's rank functions, re-export, refresh.
- **To change the UI:** edit `ui/components.py` (shared layout) or the individual pages.
"""
)

footer()
