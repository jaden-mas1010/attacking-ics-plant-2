#!/usr/bin/env python3
# Modbus Scanner – ICS Plant #2

from pymodbus.client.sync import ModbusTcpClient

target_ip = "192.168.100.10"
client = ModbusTcpClient(target_ip)

print(f"[+] Scanning Modbus device at {target_ip}")

if client.connect():
    try:
        # Read coils
        coils = client.read_coils(0, 10)
        print("[+] Coils:", coils.bits)

        # Read holding registers
        regs = client.read_holding_registers(0, 10)
        print("[+] Holding Registers:", regs.registers)

    except Exception as e:
        print("[-] Error:", e)

    client.close()
else:
    print("[-] Unable to connect to Modbus device")
