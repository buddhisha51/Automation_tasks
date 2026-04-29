from netmiko import ConnectHandler
import datetime

device = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',       
    'username': 'developer',       
    'password': 'C1sco12345',
    'port': '22'
}
print ("connecting")
connection = ConnectHandler(**device)
print ("connected")

print("downloading currunt config")
full_config = connection.send_command ("show run")
print(f"Captured {len(full_config)} characters of config.")

date = datetime.date.today()
filename = f"backup-router-{date}.txt"
print(f"creating file - {filename}")

with open (filename, 'w') as save_file:
    save_file.write(full_config)

print("Backup Complete! Check your folder.")
connection.disconnect()