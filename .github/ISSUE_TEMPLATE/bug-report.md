---
name: Bug Report
description: Something doesn't work
title: "[Bug] Short description"
labels: ["bug", "triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: What happened?
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction steps
