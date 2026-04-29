from netmiko import ConnectHandler

# 1. Define the device details (The "Target")
cisco_sandbox = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'username': 'developer', 
    'password': 'C1sco12345',
    'port': 22,
}

print("Connecting to the sandbox router... please wait.")

# 2. Establish the SSH connection (The "Handshake")
connection = ConnectHandler(**cisco_sandbox)

print("Success! Connection established.")

# 3. Send a command
output = connection.send_command("show run")

# 4. Print the result
print(output)


# 5. Close the connection
connection.disconnect()
