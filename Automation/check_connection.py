from netmiko import ConnectHandler

# 1. Define the device details (The "Target")
Device = {
    'device_type': 'aruba_aoscx',
    'host': '192.168.2.233',
    'username': 'admin', 
    'password': 'admin@123',
    'port': 22,
}

print("Connecting to the switch... please wait.")

# 2. Establish the SSH connection (The "Handshake")
connection = ConnectHandler(**Device)

print("Success! Connection established.")

# 5. Close the connection
connection.disconnect()
