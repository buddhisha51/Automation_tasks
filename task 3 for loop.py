from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',       
    'username': 'developer',       
    'password': 'C1sco12345',
    'port': '22'
}

connection = ConnectHandler(**device)
print ("connected")
 
for n in range(101, 106):
 print(f"configuring loopback {n}...")

 config = [
  f'interface loopback{n}',
  f'description looped{n}',
  f'ip address 172.16.28.{n} 255.255.255.255',
  'no shut'
 ]
 output = connection.send_config_set(config)
 print(output)
print("checking...")
output2 = connection.send_command("show ip int brief | include Loopback")
print(output2)
connection.save_config()
connection.disconnect()
print("done!")


