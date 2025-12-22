# examples/quickstart/test_engine.py
import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
print(f"Adding repo root to sys.path: {repo_root}")
sys.path.insert(0, repo_root)
actions_path = os.path.join(repo_root, 'actions', 'energy', 'starter_actions.yaml')
baseline_path = os.path.join(repo_root, 'examples', 'quickstart', 'plant_energy_baseline.csv')

from src.core.engine.sustainaction import SustainActionEngine

if __name__ == "__main__":
    engine = SustainActionEngine(actions_path=actions_path)
    actions = engine.match_actions(baseline_path)
    
    print("=== PAGIR SustainAction Results ===\n")
    for action in actions:
        print(f"🎯 {action['name']}")
        print(f"  Assets: {action.get('asset_count', 0)} ({', '.join(action.get('assets', []))})")
        print(f"  Savings: {action['estimated_savings_kwh']:,} kWh | {action['estimated_savings_co2e']} tCO₂e")
        print()
