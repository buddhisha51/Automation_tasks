from netmiko import ConnectHandler

device = {
'device_type': 'cisco_ios',
    'host': '10.10.20.48',       
    'username': 'developer',       
    'password': 'C1sco12345',
    'port': '22'
}
connection = ConnectHandler(**device)
print("connected")

for n in range (200, 206):
    if n == 203:
        print (f"loopback {n} is reserved")
        continue
    print(f"configuring loopback {n}")

    config = [
        f'interface loopback{n}',
        f'description Automation_Lesson_4_ID_{n}',
        f'ip address 172.16.200.{n} 255.255.255.255',
        'no shut'
        ]
    connection.send_config_set(config)
print ("verifying")
output = connection.send_command('show ip int brief | include Loopback20')
print (output)

connection.disconnect()
print("done")