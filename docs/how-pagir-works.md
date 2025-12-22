# How PAGIR Works

PAGIR helps organizations move from high-level sustainability targets to concrete, trackable actions in four steps.

---

## 1. Understand baselines and goals

- Import simple baseline data such as plant energy use, major motor and compressor loads, and production volumes (initially via CSV, later via meters/IIoT).
- Capture existing targets (e.g., “20% energy reduction by 2028”, “net‑zero by 2040”) and select relevant frameworks (GRI, TCFD, BRSR, CSRD) so actions and metrics stay aligned with reporting needs.

---

## 2. Translate targets into actions (SustainAction)

- Use the SustainAction engine and open action libraries (starting with energy-efficiency actions for motors, pumps, fans, compressors, and utilities) to generate a list of candidate measures. 
- For each measure, PAGIR associates owners, suggested timelines, and estimated impact (kWh and CO₂e saved per year), giving organizations a prioritized “targets → actions” map instead of a generic checklist.

---

## 3. Connect to real-world data and track

- Link actions and KPIs to data sources: spreadsheets in the simplest case, and later energy meters, IIoT/SCADA signals, or other monitoring systems.
- Convert raw data into progress indicators (e.g., energy use vs baseline, realized CO₂e savings vs estimates), with data-quality flags so users know how much confidence to place in each metric.

---

## 4. Report, learn, and improve the commons

- Generate draft ESG / sustainability outputs aligned with chosen frameworks, including tables and narrative text that can be refined for board reports, disclosures, or CSR communication. 
- Optionally share anonymized patterns (for example, “VFD retrofit on similar pumps typically saves 20–30% energy”) back into the open libraries, so future users benefit from real-world experience without exposing sensitive data.

## Example use case: Ajith at a factory

This example shows how a factory energy & sustainability manager might use PAGIR end to end.

### Persona

**Name:** Ajith  
**Role:** Energy & Sustainability Manager at a mid-sized manufacturing plant in India  

**Context:**

- Plant has 50+ motors, 2 main compressors, several pumps and fans, where energy efficiency is a key driver of cost and environmental performance.[web:419]  
- Management target: **“Reduce electricity use by 20% by 2028 and start ESG reporting (BRSR).”**[web:426]  
- Data is scattered: energy bills, Excel sheets, occasional SCADA screenshots.  
- Limited time, no dedicated data science team.

---

### Ajith’s journey with PAGIR

1. **Set up baselines and goals**

   - Ajith exports a simple CSV listing major assets and annual electricity use and uploads this as his baseline.  
   - In the UI / notebook, he enters:
     - Target: “20% plant electricity reduction by 2028”  
     - Frameworks: “BRSR + internal management reporting”, aligned with broader frameworks like GRI and TCFD where needed.

2. **Get a first action plan with SustainAction**

   - The SustainAction engine reads the baseline and matches it against energy action templates (for example, VFD retrofits for motors, compressed-air leak management, and motor rightsizing), which are common measures in industrial plants.[web:419]  
   - PAGIR suggests actions such as:
     - Install VFDs on oversized constant-speed motors (fans, pumps).  
     - Establish compressed-air leak detection and repair.  
     - Rightsize continuously lightly loaded motors.  
   - Each suggestion includes a short description, estimated impact (kWh and tCO₂e per year), and fields for owner and timeline that Ajith can fill in.

3. **Connect to data and track progress**

   - Initially, Ajith updates a simple CSV each month with new energy readings and reruns the notebook to refresh KPIs.  
   - PAGIR shows:
     - Current energy vs baseline.  
     - Realized savings vs estimated savings per action, similar to how many plants now track pump and compressor performance with digital tools.
   - Later, an engineer configures an IIoT or meter integration so data flows automatically from the plant systems.

4. **Generate reports and communicate**

   - Each quarter, Ajith uses PAGIR to:
     - Export a BRSR-aligned table of energy use and completed actions.
     - Generate draft narrative text summarizing what actions were taken, why they were chosen, and the impact achieved in kWh and CO₂e.  
   - He refines this text and includes it in board reports and ESG disclosures, ensuring consistency across frameworks like BRSR and GRI.

5. **Learn and improve over time**

   - As more actions are completed, Ajith sees which ones deliver the expected savings and adjusts future plans.  
   - He can optionally allow anonymized results (for example, “VFD on 11 kW pump → 22% energy saved”) to improve shared action evidence, which helps similar factories choose better measures over time.
