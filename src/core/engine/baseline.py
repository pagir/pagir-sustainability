"""Parse factory baseline CSV → structured assets"""

import pandas as pd

def parse_baseline_csv(csv_path: str) -> pd.DataFrame:
    """Convert plant_energy_baseline.csv → assets DataFrame"""
    df = pd.read_csv(csv_path)
    # Expected columns: id, type, power_kw, annual_kwh, location
    return df
