from netmiko import ConnectHandler

# 1. Define the device details (The "Target")
Device = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'username': 'developer', 
    'password': 'C1sco12345',
    'port': 22,
}

print("Connecting to the switch... please wait.")

# 2. Establish the SSH connection (The "Handshake")
connection = ConnectHandler(**Device)

print("Success! Connection established.")
print("connected")

# 5. Close the connection
connection.disconnect()
