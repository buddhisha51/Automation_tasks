from netmiko import ConnectHandler

cisco_sandbox = {
'device_type':  'cisco_ios',
'host': '10.10.20.48',
'username': 'developer',
'password': 'C1sco12345',
'port': '22',
}

print("connecting to router...")
connection = ConnectHandler(**cisco_sandbox)
print("connected")
config_commands = [
    'interface loopback 99',
    'description configured by python bot',
    'ip addr 172.16.99.1 255.255.255.255',
    'no shut',
    'exit',
    'exit',
    'show ip interface brief | include Loopback99'
]
output = connection.send_config_set(config_commands)

print(output)
print("\nsaving the commands")
saving = connection.send_command("write")

connection.disconnect()
print("done!")