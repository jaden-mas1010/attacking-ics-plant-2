# PLC Register Map – ICS Plant #2
## Modbus Coils & Registers (Process Control Overview)

This document maps the key coils and registers used by the PLC in ICS Plant #2.  
It helps SOC analysts, engineers, and red teamers understand how process values and actuators are controlled.

---

## 1. Coil Map (Digital Outputs)

| Coil Address | Description | Normal State | Notes |
|--------------|-------------|--------------|-------|
| 0 | Main Pump Control | ON | Critical actuator |
| 1 | Valve A Control | OFF | Controls flow direction |
| 2 | Valve B Control | OFF | Secondary routing |
| 3 | Alarm Output | OFF | Triggers plant alarm |
| 4 | Safety Interlock | ON | Must remain active |
| 5 | Process Stop Command | OFF | Used in shutdown attacks |
| 6–9 | Spare Coils | Varies | Unused / test coils |

---

## 2. Holding Registers (Process Values)

| Register Address | Description | Typical Value | Notes |
|------------------|-------------|----------------|-------|
| 0 | Tank Level (%) | 45–60 | Main process variable |
| 1 | Flow Rate (L/min) | 120–180 | Pump output measurement |
| 2 | Pressure (kPa) | 300–450 | Critical safety metric |
| 3 | Fill Setpoint (%) | 55 | Target tank level |
| 4 | Drain Setpoint (%) | 20 | Minimum safe level |
| 5 | Temperature (°C) | 40–55 | Process heating |
| 6 | Safety Threshold | 500 | Max pressure limit |
| 7–9 | Spare Registers | Varies | Often unused |

---

## 3. Input Registers (Sensor Readings)

| Input Register | Description | Typical Value | Notes |
|----------------|-------------|----------------|-------|
| 100 | Temperature Sensor | 40–55 | Mirrors holding register 5 |
| 101 | Pressure Sensor | 300–450 | Mirrors holding register 2 |
| 102 | Flow Sensor | 120–180 | Mirrors holding register 1 |

---

## 4. Critical Attack Points

### ✔ Setpoint Manipulation  
Registers **3** and **4** directly control tank fill/drain behavior.

### ✔ Process Shutdown  
Coils **0**, **1**, **2**, and **5** can stop pumps and valves.

### ✔ Safety Override  
Register **6** controls pressure limits — dangerous if modified.

---

## 5. Analyst Notes

- Modbus has **no authentication**, so any host can read/write these values.
- Monitoring write operations to coils and registers is essential.
- Baseline values should be stored for anomaly detection.
- Changes to setpoints or safety thresholds should trigger high‑severity alerts.

---

## 6. Purpose

This register map supports:
- SOC alerting  
- Forensic analysis  
- Red team documentation  
- Engineering validation  
- Detection rule tuning  

