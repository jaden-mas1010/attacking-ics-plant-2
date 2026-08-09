# Attacker Chain – Attacking ICS Plant #2

This attacker chain documents how an adversary can compromise an ICS environment, enumerate PLC logic, manipulate process values, and disrupt industrial operations using insecure-by-design protocols such as Modbus.

---

## 1. Reconnaissance

The attacker begins by discovering ICS devices exposed on the network.

Key actions:
- Scan for TCP port **502** (Modbus)
- Identify PLC type and responsiveness
- Enumerate coils, holding registers, and input registers
- Map the PLC’s memory layout

Outcome:
The attacker gains full visibility into the PLC’s process variables and control logic.

---

## 2. Modbus Interaction

Once the PLC is identified, the attacker interacts with it using standard Modbus function codes.

Common operations:
- **FC01 – Read Coils** (digital outputs)
- **FC03 – Read Holding Registers** (process values)
- **FC05 – Write Single Coil** (toggle actuators)
- **FC06 – Write Single Register** (change process parameters)
- **FC16 – Write Multiple Registers** (bulk manipulation)

Outcome:
The attacker learns which registers control pumps, valves, setpoints, and tank levels.

---

## 3. Process Manipulation

The attacker begins altering process values to influence physical behaviour.

Examples:
- Changing tank fill setpoints
- Modifying pump activation thresholds
- Overwriting safety limits
- Forcing coils ON/OFF to control actuators

Scripts used:
- `attack_stop_process.py`
- `attack_change_setpoints.py`
- `attack_shutdown.py`

Outcome:
The attacker can directly manipulate the industrial process without authentication.

---

## 4. Disruption & Impact

By abusing Modbus write operations, the attacker can:

- Stop critical pumps
- Overfill or underfill tanks
- Trigger fault conditions
- Cause process shutdowns
- Create unsafe operating states

Impact:
Loss of control, operational downtime, and potential physical damage.

---

## 5. SOC Detection Opportunities

SOC analysts can detect malicious ICS activity by monitoring:

- Unexpected Modbus write operations
- Access from non-ICS network segments
- Abnormal function code usage (FC05, FC06, FC16)
- High-frequency register polling
- Deviations from normal coil/register patterns

Detection rules (Suricata/Sigma) are included in the `detection_rules/` folder.

---

## 6. Summary

This attacker chain demonstrates how insecure ICS protocols like Modbus can be abused to manipulate industrial processes. The challenge highlights the importance of monitoring OT networks, enforcing segmentation, and detecting unauthorized write operations.

