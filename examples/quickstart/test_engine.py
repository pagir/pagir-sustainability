# examples/quickstart/test_engine.py
from src.core.engine.sustainaction import SustainActionEngine

if __name__ == "__main__":
    engine = SustainActionEngine()
    actions = engine.match_actions("plant_energy_baseline.csv")
    
    print("=== PAGIR SustainAction Results ===\n")
    for action in actions:
        print(f"Action: {action['name']}")
        print(f"  Assets: {len(action['assets'])} ({', '.join(action['assets'])})")
        print(f"  Savings: {action['estimated_savings_kwh']:,} kWh | {action['estimated_savings_co2e']} tCO₂e")
        print()
