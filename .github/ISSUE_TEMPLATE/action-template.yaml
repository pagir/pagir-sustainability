---
name: Action Template
description: Add new sustainability action (motors, HVAC, regen practices)
title: "[Action] Short name - [Domain]"
labels: ["action-template", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        **Highest impact contribution.** Add battle-tested action → Flywheel turns.

  - type: dropdown
    id: domain
    attributes:
      label: Domain
      options:
        - energy
        - agriculture
        - products
        - cities
        - other
    validations:
      required: true

  - type: textarea
    id: action-details
    attributes:
      label: Action Details (YAML format)
      placeholder: |
        name: "Motor VFD Retrofit"
        savings_tCO2e: "50-150" 
        cost_eur: "3000-8000"
        roi_months: "12-18"
        verification: ["meter", "invoice"]
        references: ["Study XYZ", "Factory A pilot"]
      render: yaml
    validations:
      required: true

  - type: textarea
    id: evidence
    attributes:
      label: Evidence (2+ sources)
      placeholder: "Link to study/invoice/pilot data"
