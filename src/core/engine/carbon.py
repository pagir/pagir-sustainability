"""CO₂e calculations for India grid"""

GRID_EMISSION_FACTOR_IN = 0.8  # kgCO₂e/kWh (2025 estimate)

def kwh_to_co2e(kwh: float, factor: float = GRID_EMISSION_FACTOR_IN) -> float:
    """Convert kWh saved → tCO₂e"""
    return round((kwh * factor) / 1000, 1)  # tonnes
