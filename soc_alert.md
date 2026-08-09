# SOC Alert – Malicious Modbus Write Activity
## Industrial Control System (ICS) – Attacking ICS Plant #2

**Alert ID:** ICS-MODBUS-WRITE-001  
**Severity:** High  
**Category:** Unauthorized Control Command  
**Protocol:** Modbus/TCP  
**Source:** Network IDS / ICS Monitoring Stack  

---

## 1. Summary

The SOC has detected unauthorized Modbus write operations targeting a PLC controlling critical processes inside ICS Plant #2. The activity indicates an adversary attempting to manipulate coils and holding registers, potentially disrupting physical operations.

---

## 2. Detection Details

**Observed Behavior:**
- Multiple Modbus function codes associated with write operations:
  - **FC05 – Write Single Coil**
  - **FC06 – Write Single Register**
  - **FC16 – Write Multiple Registers**
- Writes issued from a non‑ICS network segment
- High‑frequency polling followed by sudden register manipulation
- Attempts to modify setpoints and actuator states

**Indicators:**
- Unexpected coil toggles (ON/OFF)
- Register values overwritten outside normal operating ranges
- Commands issued from unauthorized IP addresses

---

## 3. Impact Assessment

Potential consequences include:
- Forced pump shutdowns
- Overfilling or draining tanks
- Manipulation of safety thresholds
- Triggering fault conditions
- Full process disruption or shutdown

This activity represents a direct threat to operational continuity and physical safety.

---

## 4. Recommended SOC Actions

### Immediate Actions
- Isolate the source IP from ICS network segments
- Block Modbus/TCP traffic from unauthorized hosts
- Notify OT/ICS engineering teams
- Capture full packet traces for forensic analysis

### Investigation Steps
- Review PLC logs for unauthorized writes
- Validate current coil/register states
- Compare register values against baseline
- Check for lateral movement attempts

### Long-Term Mitigation
- Enforce network segmentation between IT and OT
- Deploy Modbus-aware intrusion detection rules
- Implement write‑operation whitelisting
- Monitor for abnormal function code usage

---

## 5. Evidence

Packet captures and screenshots are stored in:

