# Final Report – Attacking ICS Plant #2
## Full Case Study: Reconnaissance → Exploitation → Impact → Detection → Mitigation

This report documents the complete attack lifecycle executed against ICS Plant #2.  
It covers reconnaissance, Modbus exploitation, PLC manipulation, operational impact, detection logic, and defensive recommendations.

---

# 1. Executive Summary

ICS Plant #2 is a simulated industrial environment using a PLC that communicates via Modbus/TCP.  
The challenge demonstrates how insecure-by-design industrial protocols allow attackers to manipulate physical processes without authentication.

Key findings:
- PLC exposed on TCP port 502
- Modbus protocol lacks authentication and encryption
- Coils and registers directly control pumps, valves, setpoints, and safety thresholds
- Unauthorized write operations allow full process manipulation
- Weak segmentation enables IT → OT lateral movement

Outcome:
The attacker successfully enumerated PLC memory, modified process values, and disrupted operations.

---

# 2. Environment Overview

### Components:
- Corporate IT network (weakly segmented)
- ICS control network (EWS, HMI, Historian)
- PLC running Modbus/TCP
- Physical equipment (pumps, valves, sensors, tanks)

### Protocol:
- **Modbus/TCP (Port 502)**  
- No authentication  
- No encryption  
- No integrity checking  

### PLC Memory:
- Coils → digital outputs (actuators)
- Holding registers → process values (setpoints, levels, pressure)
- Input registers → sensor readings

---

# 3. Attacker Chain Summary

### 3.1 Reconnaissance
- Scanned network for port 502
- Identified PLC responding to Modbus queries
- Enumerated coils and registers
- Mapped critical process variables

### 3.2 Exploitation
Used Modbus function codes:
- **FC01** – Read Coils  
- **FC03** – Read Holding Registers  
- **FC05** – Write Single Coil  
- **FC06** – Write Single Register  
- **FC16** – Write Multiple Registers  

### 3.3 Process Manipulation
Examples:
- Turning pumps OFF  
- Changing tank fill setpoints  
- Overwriting safety thresholds  
- Triggering alarms  

Scripts used:
- `modbus_write.py`
- `attack_stop_process.py`
- `attack_change_setpoints.py`
- `attack_shutdown.py`

### 3.4 Impact
- Loss of control over pumps and valves  
- Unsafe tank levels  
- Pressure threshold manipulation  
- Potential physical damage  
- Full process shutdown  

---

# 4. Technical Evidence

### 4.1 Coils (Actuators)
Critical coils:
- 0 → Main pump  
- 1 → Valve A  
- 2 → Valve B  
- 5 → Process stop  

### 4.2 Registers (Process Values)
Critical registers:
- 0 → Tank level  
- 1 → Flow rate  
- 2 → Pressure  
- 3 → Fill setpoint  
- 6 → Safety threshold  

### 4.3 Packet Captures
Stored in:
/evidence/packet-captures/

Code

### 4.4 Scripts
Stored in:
/scripts/

Code

---

# 5. Detection Analysis

### Indicators of Compromise:
- Unauthorized Modbus write operations  
- Function codes 5, 6, 16  
- High-frequency polling  
- Writes from non-ICS network segments  
- Register values outside baseline  
- Coil toggles during non-operational hours  

### Detection Rules:
- Suricata IDS rules  
- Sigma SIEM rules  
- Splunk `.spl` correlation search  

Stored in:
/detection_rules/

Code

---

# 6. Root Cause Analysis

### Primary Causes:
1. **Weak Network Segmentation**  
   IT network could reach OT network directly.

2. **Insecure Protocol (Modbus)**  
   No authentication → attacker can write to PLC memory.

3. **Lack of Monitoring**  
   No IDS/IPS or anomaly detection on ICS network.

4. **Predictable PLC Memory Layout**  
   Standard Modbus mapping makes enumeration trivial.

---

# 7. Mitigation Recommendations

### 7.1 Immediate Actions
- Block unauthorized IPs from accessing port 502  
- Isolate PLC from corporate network  
- Reset manipulated coils and registers  
- Validate setpoints and safety thresholds  

### 7.2 Medium-Term Actions
- Deploy ICS-aware IDS (Suricata, Zeek, Nozomi, Claroty)  
- Implement write-operation whitelisting  
- Enforce strict network segmentation  
- Monitor Modbus function codes  

### 7.3 Long-Term Actions
- Migrate to secure industrial protocols  
- Implement role-based access control  
- Deploy anomaly detection for process values  
- Conduct regular ICS penetration tests  

---

# 8. Conclusion

ICS Plant #2 demonstrates how insecure industrial protocols and weak segmentation allow attackers to manipulate physical processes with minimal effort.  
By enumerating coils and registers and issuing unauthorized write commands, the attacker gained full control over pumps, valves, setpoints, and safety thresholds.

This case study highlights the importance of:
- Monitoring OT networks  
- Enforcing segmentation  
- Detecting unauthorized Modbus writes  
- Understanding PLC memory structures  

The repository provides a complete attacker chain, detection logic, scripts, and documentation to support SOC analysts, engineers, and red teamers.
