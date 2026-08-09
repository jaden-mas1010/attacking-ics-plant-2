#!/usr/bin/env python3
# Modbus Write Tool – ICS Plant #2

from pymodbus.client.sync import ModbusTcpClient

target_ip = "192.168.100.10"
client = ModbusTcpClient(target_ip)

coil_address = 0
register_address = 1

print(f"[+] Connecting to PLC at {target_ip}")

if client.connect():
    try:
        print("[+] Writing coil ON")
        client.write_coil(coil_address, True)

        print("[+] Writing register value 999")
        client.write_register(register_address, 999)

    except Exception as e:
        print("[-] Error:", e)

    client.close()
else:
    print("[-] Connection failed")
