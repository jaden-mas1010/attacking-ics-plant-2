# Attacking ICS Plant #2

This repository contains my personal analysis, scripts, and SOC-focused documentation from the *Attacking ICS Plant #2* challenge. It explores how insecure industrial protocols and poorly protected PLC logic can be abused to manipulate physical processes inside an ICS environment.

## Overview

ICS/OT environments often rely on legacy protocols such as Modbus, which lack authentication, encryption, and integrity controls. This challenge demonstrates how attackers can:

- Enumerate PLC registers
- Interact with coils and holding registers
- Modify process values
- Disrupt or shut down industrial operations

This repository includes only my own work, analysis, and scripts.

## Contents

- **attacker_chain.md** – Full attacker chain from recon → exploitation → impact  
- **soc_alert.md** – SOC-style alert for malicious Modbus activity  
- **detection_rules/** – Suricata and Sigma rules for detection  
- **scripts/** – Python scripts used to interact with the PLC  
- **notes/** – Protocol breakdown and PLC register mapping  
- **evidence/** – Packet captures and screenshots

## Why This Matters

ICS/OT attacks are increasingly common, and SOC analysts must understand how insecure protocols behave and how attackers manipulate industrial processes. This case study demonstrates practical OT/ICS security knowledge applicable to real-world monitoring and incident response.

## Disclaimer

This repository contains only my own notes, analysis, and original work.  
No proprietary TryHackMe content, answers, or walkthroughs are included.
