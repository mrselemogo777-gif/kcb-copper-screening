import json
import pandas as pd
from pathlib import Path

OUT = Path("outputs")



def load_shortlist() -> pd.DataFrame:
    path = OUT / "shortlist.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run the notebook first.")
    return pd.read_csv(path)

def load_geojson(name: str):
    path = OUT / name
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)
