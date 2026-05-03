from netmiko import ConnectHandler


device = {
    'device_type': 'cisco_xr',
    'host': 'YOUR_SANDBOX_HOST',
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'port': 22,
}

print("connecting to device...")


try:
    connection = ConnectHandler(**device)
    print("Connected! Running commands...")

    output = connection.send_command('show version')
    print("\n-- Show Version ---")
    print(output)


    interfaces = connection.send_command("show ip interface brief")
    print("\n--- Interfaces ---")
    print(interfaces)


    connection.disconnect()
    print("\nDisconnected")


except Exception as e:
    print(f"Failed to connect {e}")