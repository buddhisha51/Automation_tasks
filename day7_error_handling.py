from netmiko import ConnectHandler
Device_list = [{
        'device_type': 'cisco_ios',
        'host': '192.168.99.99',     
        'username': 'admin',
        'password': 'password',
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.10.20.48',      
        'username': 'developer',
        'password': 'C1sco12345',
        'port': 22,
    },
    {
        'device_type': 'cisco_ios',
        'host': '1.1.1.1',           
        'username': 'admin',
        'password': 'password',
    }]

print('starting batch job')
for device in Device_list :
    print (f'\n...........................')
    print (f'connecting to {device['host']}')
    try:
        connection = ConnectHandler(**device)
        print(f'successfully connected to device {device['host']}')
        print(connection.send_command("show version | include Uptime"))
        connection.disconnect()
    except Exception as err:
        print(f'connection failed to {device['host']} with erro {err}')

print("\n............................")
print("Job Complete. The script survived!")


        
        