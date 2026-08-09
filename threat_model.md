# Threat Model – ICS Plant #2
## STRIDE + ICS-Specific Threat Analysis for Modbus/TCP Environments

This threat model identifies adversaries, attack vectors, vulnerable components, and potential impacts within ICS Plant #2.  
It uses a hybrid approach combining STRIDE, ICS-specific threat categories, and real-world OT attack patterns.

---

# 1. System Overview

ICS Plant #2 consists of:
- Corporate IT network
- ICS control network (EWS, HMI, Historian)
- PLC using Modbus/TCP
- Physical equipment (pumps, valves, sensors, tanks)

Primary protocol:
- **Modbus/TCP (Port 502)** — insecure by design

Primary assets:
- PLC coils (actuators)
- PLC registers (process values)
- Engineering workstation
- ICS network segmentation
- Physical process integrity

---

# 2. Threat Actors

### 2.1 Opportunistic Attackers
- Scan internet/internal networks for exposed ICS devices
- Exploit insecure protocols without deep ICS knowledge

### 2.2 Insider Threats
- Engineers or operators with legitimate access
- Can modify setpoints or disable safety systems

### 2.3 Skilled Adversaries (Red Teams / APT)
- Understand ICS protocols and process logic
- Target operational disruption or sabotage

### 2.4 Malware / Worms
- ICS-targeting malware (e.g., Stuxnet-like behavior)
- Spread laterally from IT → OT networks

---

# 3. Attack Surface

### 3.1 Network Exposure
- Weak segmentation allows IT → OT access
- PLC reachable directly on port 502

### 3.2 Insecure Protocol (Modbus)
- No authentication
- No encryption
- No integrity checking
- Full read/write access to PLC memory

### 3.3 Predictable Memory Layout
- Coils and registers follow standard Modbus mapping
- Easy enumeration of critical process variables

### 3.4 Engineering Workstation
- High-privilege access
- Often poorly monitored
- Single point of failure for PLC writes

---

# 4. STRIDE Threat Analysis

### **S – Spoofing**
- Attacker impersonates engineering workstation
- Sends write commands to PLC
- PLC cannot verify identity

### **T – Tampering**
- Unauthorized modification of:
  - Coils (pump/valve control)
  - Registers (setpoints, thresholds)
  - Safety limits

### **R – Repudiation**
- No audit logs for Modbus writes
- Attacker actions cannot be traced reliably

### **I – Information Disclosure**
- Attacker reads:
  - Tank levels
  - Pressure values
  - Flow rates
  - Safety thresholds

### **D – Denial of Service**
- Flooding PLC with Modbus requests
- Overwriting critical coils to OFF
- Setting unsafe register values

### **E – Elevation of Privilege**
- Any host can perform engineering-level writes
- No role-based access control

---

# 5. ICS-Specific Threat Categories

### **Loss of View**
Attacker manipulates sensor values or HMI data:
- False tank levels
- Incorrect pressure readings
- Misleading flow rates

### **Loss of Control**
Attacker manipulates actuators:
- Pumps OFF
- Valves OPEN/CLOSE
- Safety interlocks disabled

### **Process Manipulation**
Attacker changes setpoints:
- Overfill tanks
- Overpressure pipes
- Overheat process loops

### **Physical Damage**
Possible outcomes:
- Equipment failure
- Tank overflow
- Pipe rupture
- Safety system bypass

---

# 6. Attack Scenarios

### **Scenario 1: Unauthorized Modbus Write**
- Attacker writes coil 0 → pump OFF
- Process halts unexpectedly

### **Scenario 2: Setpoint Manipulation**
- Register 3 changed from 55% → 1200%
- Tank overfills → spill or damage

### **Scenario 3: Safety Threshold Override**
- Register 6 changed from 500 → 9999
- Pressure exceeds safe limits → rupture risk

### **Scenario 4: Reconnaissance + Lateral Movement**
- Attacker scans IT network
- Moves laterally into OT network
- Enumerates PLC memory
- Executes write operations

---

# 7. Impact Assessment

### Operational Impact
- Production downtime
- Loss of control over critical equipment
- Unsafe operating conditions

### Safety Impact
- Risk to personnel
- Equipment damage
- Environmental hazards

### Financial Impact
- Repair costs
- Regulatory fines
- Lost production

### Reputational Impact
- Loss of trust in ICS operations
- Compliance violations

---

# 8. Defensive Controls (Summary)

See `blue_team_hardening.md` for full details.

Key controls:
- Strict IT/OT segmentation
- Modbus write-operation monitoring
- ICS-aware IDS (Suricata, Zeek)
- Engineering workstation hardening
- Role-based access control
- Baseline anomaly detection

---

# 9. Threat Model Summary

ICS Plant #2 is vulnerable due to:
- Insecure Modbus protocol
- Weak segmentation
- Lack of monitoring
- Predictable PLC memory layout

Attackers can:
- Enumerate coils/registers
- Issue unauthorized write commands
- Manipulate physical processes
- Cause operational disruption or damage

This threat model provides a structured understanding of risks and supports defensive planning, SOC monitoring, and red-team analysis.

