---
name: genpark-personal-agent-respiratory-co2-tolerance-bolti-skill
version: "1.0.0"
description: "Zero-dependency Body Oxygen Level Test (BOLT) calculator, Bohr effect tissue oxygenation modeler, hypercapnic chemoreceptor sensitivity tracker, and Buteyko breathing scheduler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Respiratory CO2 Tolerance BOLT Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to optimize human respiratory biochemistry, measure arterial carbon dioxide tolerance via the Body Oxygen Level Test (BOLT), quantify Bohr effect tissue oxygenation, and prescribe Buteyko breathwork protocols.

## Agent In-Context Capabilities

- **Bohr Effect Oxygen Delivery Modeling**: Quantifies how arterial pCO2 levels shift the hemoglobin dissociation curve to unload oxygen to brain and muscle tissue.
- **Chemoreceptor Hypersensitivity Auditing**: Detects chronic subclinical hyperventilation and elevated resting minute ventilation (>8 L/min).
- **Conditioning Progression**: Formulates micro-pause nasal breathing intervals and nocturnal mouth taping protocols to raise BOLT scores toward 40 seconds.

## Tools Summary

1. `evaluate_bolt_respiratory_efficiency`: Assesses BOLT score, minute ventilation, and Bohr multiplier.
2. `generate_reduced_breathing_schedule`: Prescribes Buteyko breath exercises and air hunger drills.
