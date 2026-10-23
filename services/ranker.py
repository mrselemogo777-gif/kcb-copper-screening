import pandas as pd

RANK_COL = {
    "Conservative": "rank_anchor",
    "Default": "rank_default",
    "Exploratory": "rank_copper",
    "Consensus only": "rank_default",
}

def filter_by_posture(df: pd.DataFrame, posture: str):
    rank_col = RANK_COL[posture]
    view = df[df["label"] == "Consensus"].copy() if posture == "Consensus only" else df.copy()
    view = view.sort_values(rank_col).reset_index(drop=True)
    return view, rank_col
