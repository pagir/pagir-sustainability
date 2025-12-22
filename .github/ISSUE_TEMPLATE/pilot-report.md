---
name: Pilot Report
description: Share real-world results (tCO₂e verified)
title: "[Pilot] Org type - tCO₂e verified"
labels: ["pilot", "verification", "high-priority"]
body:
  - type: markdown
    attributes:
      value: |
        **Truth engine.** Verified outcomes improve recommendations for 1,000+ orgs.

  - type: textarea
    id: organization
    attributes:
      label: Organization (anonymized OK)
      placeholder: "Factory A (Chennai motors)"

  - type: textarea
    id: baseline
    attributes:
      label: Baseline Data
      placeholder: "Annual energy: 2.5 GWh | Motors: 65% load"

  - type: textarea
    id: actions-taken
    attributes:
      label: Actions Implemented
      placeholder: "VFD on 12 motors | Submetering line 2"

  - type: textarea
    id: verified-impact
    attributes:
      label: Verified tCO₂e
      placeholder: "Metered: 25k tCO₂e/year | Confidence: 85%"
