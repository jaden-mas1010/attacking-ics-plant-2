# Modbus Protocol Breakdown – ICS Plant #2
## Understanding Coils, Registers, and Function Codes

This document explains how Modbus/TCP works inside ICS Plant #2, how PLC memory is structured, and how attackers abuse insecure-by-design protocol behavior.

---

## 1. What is Modbus?

Modbus is a legacy industrial protocol used for communication between PLCs, sensors, and HMIs.  
It is **insecure by design**:
- No authentication  
- No encryption  
- No integrity checking  
- Any host can read/write process values  

This makes Modbus a prime target for ICS attacks.

---

## 2. PLC Memory Structure

Modbus organizes PLC memory into four key areas:

### 1. **Coils (0xxxx)**  
Digital outputs (ON/OFF).  
Used to control pumps, valves, alarms, interlocks.

### 2. **Discrete Inputs (1xxxx)**  
Digital inputs (read-only).  
Used for switches, limit sensors, binary states.

### 3. **Holding Registers (4xxxx)**  
Read/write numerical values.  
Used for setpoints, tank levels, flow rates, pressure.

### 4. **Input Registers (3xxxx)**  
Read-only numerical values.  
Used for sensor readings.

ICS Plant #2 uses coils and holding registers heavily for process control.

---

## 3. Modbus Function Codes (FC)

Function codes define what operation is being performed.

### ✔ **FC01 – Read Coils**  
Used to read actuator states.

### ✔ **FC03 – Read Holding Registers**  
Used to read process values.

### ✔ **FC05 – Write Single Coil**  
Used to toggle pumps, valves, alarms.  
**Critical for shutdown attacks.**

### ✔ **FC06 – Write Single Register**  
Used to change setpoints or thresholds.

### ✔ **FC16 – Write Multiple Registers**  
Used for bulk manipulation of process values.

These write operations are the core of ICS Plant #2 exploitation.

---

## 4. Normal ICS Behavior

In a legitimate ICS environment:
- Engineering workstations issue writes  
- HMIs issue reads  
- PLCs respond deterministically  
- Network traffic is predictable and low-noise  
- Writes occur rarely and only from trusted hosts

Any deviation from this pattern is suspicious.

---

## 5. Malicious Behavior in ICS Plant #2

Attackers typically:
1. Scan for port **502**  
2. Enumerate coils and registers  
3. Identify critical process variables  
4. Issue unauthorized write commands  
5. Manipulate physical operations

Examples:
- Turning pumps OFF  
- Changing tank fill setpoints  
- Overwriting safety thresholds  
- Triggering alarms or shutdowns  

This is exactly what the scripts in `/scripts/` demonstrate.

---

## 6. Why Modbus is Dangerous

Modbus lacks:
- Authentication  
- Authorization  
- Encryption  
- Integrity checks  
- Role-based access control  

This means:
**Any host can fully control the PLC if it can reach port 502.**

---

## 7. SOC Detection Opportunities

SOC teams should monitor:
- Unexpected Modbus write operations  
- Function codes 5, 6, 16  
- High-frequency polling  
- Writes from non-ICS network segments  
- Register values outside normal ranges  
- Coil toggles during non-operational hours  

Detection rules are included in `/detection_rules/`.

---

## 8. Summary

Modbus is simple, powerful, and dangerously insecure.  
Understanding coils, registers, and function codes is essential for detecting and responding to ICS attacks like those in ICS Plant #2.

