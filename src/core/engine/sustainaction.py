"""
PAGIR SustainAction Engine
Matches factory baselines → concrete sustainability actions
"""

import yaml
import pandas as pd
from typing import List, Dict
from .baseline import parse_baseline_csv
from .carbon import kwh_to_co2e

class SustainActionEngine:
    def __init__(self, actions_path: str = "actions/energy/starter_actions.yaml"):
        self.actions = self.load_actions(actions_path)
    
    def load_actions(self, path: str) -> List[Dict]:
        """Load action templates from YAML"""
        with open(path, 'r') as f:
            return yaml.safe_load(f)['actions']
    
    def match_actions(self, baseline_csv: str, target: str = "20% energy reduction") -> List[Dict]:
        """Core engine: baseline → prioritized actions"""
        baseline = parse_baseline_csv(baseline_csv)
        actions = []
        
        for action_template in self.actions:
            matches = self._find_matching_assets(baseline, action_template)
            if matches:
                action = self._generate_action(action_template, matches, target)
                actions.append(action)
        
        return sorted(actions, key=lambda x: x['estimated_savings_kwh'], reverse=True)
    
    def _find_matching_assets(self, baseline: pd.DataFrame, action: Dict) -> List:
        """Find assets that match action criteria (e.g. 'pump > 20kW')"""
        matches = []
        for _, asset in baseline.iterrows():
            if self._asset_matches_criteria(asset, action['criteria']):
                matches.append(asset)
        return matches
    
    def _asset_matches_criteria(self, asset: pd.Series, criteria: Dict) -> bool:
        """Check if asset fits action (e.g. type='pump', power>20)"""
        for key, value in criteria.items():
            if asset.get(key) != value:
                return False
        return True
    
    def _generate_action(self, template: Dict, assets: List, target: str) -> Dict:
        """Generate concrete action with estimates"""
        total_kwh = sum(asset['annual_kwh'] for asset in assets)
        savings_pct = template['typical_savings_pct']
        estimated_kwh = total_kwh * savings_pct
        estimated_co2e = kwh_to_co2e(estimated_kwh)
        
        return {
            'id': template['id'],
            'name': template['name'],
            'description': template['description'],
            'assets': [asset['id'] for asset in assets],
            'estimated_savings_kwh': estimated_kwh,
            'estimated_savings_co2e': estimated_co2e,
            'typical_savings_pct': savings_pct,
            'owner': None,  # User fills
            'timeline': None  # User fills
        }
