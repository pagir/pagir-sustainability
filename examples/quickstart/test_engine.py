# examples/quickstart/test_engine.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from src.core.engine.sustainaction import SustainActionEngine

if __name__ == "__main__":
    engine = SustainActionEngine("starter_actions.yaml")
    actions = engine.match_actions("plant_energy_baseline.csv")
    
    print("=== PAGIR SustainAction Results ===\n")
    for action in actions:
        print(f"🎯 {action['name']}")
        print(f"  Assets: {action.get('asset_count', 0)} ({', '.join(action.get('assets', []))})")
        print(f"  Savings: {action['estimated_savings_kwh']:,} kWh | {action['estimated_savings_co2e']} tCO₂e")
        print()
