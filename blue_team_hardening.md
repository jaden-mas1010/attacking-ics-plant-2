# Blue Team Hardening Guide – ICS Plant #2
## Defensive Controls for Preventing Modbus Exploitation and PLC Manipulation

This guide outlines practical defensive measures to protect ICS Plant #2 from unauthorized Modbus activity, PLC manipulation, and OT network compromise.  
It is designed for SOC analysts, ICS engineers, and blue‑team defenders.

---

# 1. Network Segmentation

Weak segmentation was the primary enabler of the attack.

### Required Controls:
- Strictly separate **Corporate IT** and **ICS/OT** networks
- Implement **firewall rules** blocking all IT → OT traffic by default
- Allow only:
  - Engineering Workstation → PLC
  - HMI → PLC
  - Historian → PLC
- Deny all other Modbus/TCP (port 502) traffic

### Recommended Architecture:
IT Network  →  DMZ  →  ICS Network  →  PLC

Code

### Additional Measures:
- Use VLANs to isolate OT devices
- Enforce jump servers for ICS access
- Disable routing between IT and OT unless explicitly required

---

# 2. Protocol Hardening (Modbus/TCP)

Modbus is insecure by design.  
Blue teams must compensate with monitoring and access control.

### Controls:
- Block Modbus/TCP on all non‑ICS subnets
- Restrict Modbus writes (FC05, FC06, FC16) to engineering workstation only
- Implement Modbus-aware firewalls (e.g., Tofino, Hirschmann, FortiNAC)
- Enforce read-only Modbus for HMI and Historian

### Monitoring:
- Alert on any Modbus write operation from unauthorized hosts
- Alert on abnormal function code usage
- Alert on high-frequency polling (recon behavior)

---

# 3. PLC Hardening

### Controls:
- Change default PLC passwords (if supported)
- Disable unused coils and registers
- Lock engineering workstation access behind MFA
- Enable write-protection modes (if supported)
- Regularly export and checksum PLC logic

### Physical Security:
- Restrict physical access to PLC cabinets
- Lock network switches in OT areas
- Disable unused Ethernet ports

---

# 4. Logging & Monitoring

### Deploy ICS-aware monitoring tools:
- Suricata (with Modbus rules)
- Zeek (ICS protocol analyzers)
- Nozomi Networks
- Claroty
- Security Onion (ICS sensors)

### Log the following:
- Modbus function codes
- Coil and register writes
- Engineering workstation activity
- PLC configuration changes
- Network flows between IT ↔ OT

### SIEM Integration:
Forward logs to:
- Splunk
- Elastic
- Sentinel
- QRadar

Use Sigma/Splunk rules from `/detection_rules/`.

---

# 5. Anomaly Detection

ICS environments have stable, predictable behavior.  
Anomalies are strong indicators of compromise.

### Detect:
- Register values outside normal ranges
- Coil toggles during non-operational hours
- Sudden changes in setpoints
- Pressure/flow/level deviations
- Unexpected PLC restarts
- Engineering workstation activity outside maintenance windows

### Baseline:
- Normal coil states
- Normal register values
- Normal function code usage
- Normal polling frequency

---

# 6. Access Control

### Controls:
- Role-based access control (RBAC)
- MFA for engineering workstation
- Separate credentials for IT vs OT
- Disable shared accounts
- Enforce least privilege

### Network Access:
- Only engineering workstation should have write access
- HMI should be read-only
- Historian should be read-only
- No direct PLC access from IT network

---

# 7. Incident Response for ICS

### Immediate Actions:
- Isolate malicious IPs
- Block Modbus/TCP from unauthorized hosts
- Capture packet traces
- Validate PLC coil/register states
- Restore setpoints from backup
- Notify ICS engineering team

### Forensic Actions:
- Review PLC logs
- Compare register values against baseline
- Check for lateral movement
- Validate integrity of PLC logic

### Recovery:
- Reset manipulated coils/registers
- Restore PLC configuration
- Re-enable safety thresholds
- Validate physical equipment state

---

# 8. Long-Term Hardening

### Recommended:
- Migrate to secure industrial protocols (e.g., OPC UA with encryption)
- Deploy anomaly detection ML models
- Conduct regular ICS penetration tests
- Implement secure remote access (VPN + MFA)
- Train SOC analysts on OT-specific threats
- Maintain updated asset inventory

---

# 9. Summary

ICS Plant #2 demonstrates how attackers can exploit:
- Weak segmentation  
- Insecure Modbus protocol  
- Lack of monitoring  
- Predictable PLC memory  

This hardening guide provides actionable defensive measures to prevent unauthorized PLC manipulation, detect malicious Modbus activity, and secure OT environments.

Blue teams must focus on:
- Segmentation  
- Monitoring  
- Access control  
- Protocol hardening  
- Incident response  

Securing ICS environments requires continuous vigilance and specialized defensive strategies.
