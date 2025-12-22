"""
PAGIR SustainAction Engine
Matches factory baselines → concrete sustainability actions
"""

import yaml
import pandas as pd
from typing import List, Dict, Any  # ← FIXED: Add Any here
from .baseline import parse_baseline_csv
from .carbon import kwh_to_co2e

class SustainActionEngine:
    def __init__(self, actions_path: str = "actions/energy/starter_actions.yaml"):
        self.actions = self.load_actions(actions_path)
    
    def load_actions(self, path: str) -> List[Dict[str, Any]]:
        """Load action templates from YAML"""
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data['actions']
    
    def match_actions(self, baseline_csv: str, target: str = "20% energy reduction") -> List[Dict[str, Any]]:
        """Core engine: baseline → prioritized actions"""
        baseline = parse_baseline_csv(baseline_csv)
        actions = []
        
        for template in self.actions:
            matches = self._find_matching_assets(baseline, template)
            if matches:
                action = self._generate_action(template, matches, target)
                actions.append(action)
        
        return sorted(actions, key=lambda x: x['estimated_savings_kwh'], reverse=True)
    
    def _find_matching_assets(self, baseline: pd.DataFrame, action: Dict[str, Any]) -> List[pd.Series]:
        """Find assets that match action criteria"""
        matches = []
        criteria = action.get('criteria', {})
        
        for _, asset in baseline.iterrows():
            if self._asset_matches_criteria(asset, criteria):
                matches.append(asset)
        return matches
    
    def _asset_matches_criteria(self, asset: pd.Series, criteria: Dict[str, Any]) -> bool:
        """Check if asset fits action criteria"""
        for key, value in criteria.items():
            asset_val = asset.get(key)
            
            if isinstance(value, dict):
                if 'min' in value and asset_val < value['min']:
                    return False
                if 'max' in value and asset_val > value['max']:
                    return False
            elif isinstance(value, list):
                if asset_val not in value:  # FIXED: handle list criteria (pump/fan)
                    return False
            elif asset_val != value:
                return False
        return True
    
    def _generate_action(self, template: Dict[str, Any], assets: List[pd.Series], target: str) -> Dict[str, Any]:
        """Generate concrete action with estimates"""
        total_kwh = sum(float(asset['annual_kwh']) for asset in assets)
        savings_pct = template['typical_savings_pct']
        estimated_kwh = total_kwh * savings_pct
        estimated_co2e = kwh_to_co2e(estimated_kwh)
        
        asset_ids = [asset['id'] for asset in assets]  # FIXED: proper ID extraction
        
        return {
            'id': template['id'],
            'name': template['name'],
            'description': template['description'],
            'assets': asset_ids,
            'asset_count': len(assets),  # FIXED: correct count
            'estimated_savings_kwh': round(estimated_kwh),
            'estimated_savings_co2e': estimated_co2e,
            'typical_savings_pct': savings_pct,
            'owner': None,
            'timeline': None
        }
