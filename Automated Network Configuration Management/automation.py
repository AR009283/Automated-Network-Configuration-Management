import os

devices = {
    "R-01": "192.168.1.1",
    "R-03": "192.168.2.1",
    "R-04": "192.168.4.1",
    "R-05": "192.168.5.1",
    "R-06": "192.168.7.1"
}

os.makedirs("configs", exist_ok=True)

for hostname, ip in devices.items():

    config = f"""
enable
configure terminal

hostname {hostname}

ip domain-name network.local

username admin privilege 15 secret Admin@123

ip ssh version 2

line vty 0 4
login local
transport input ssh
exit

end
write memory
"""

    filename = f"configs/{hostname}.txt"

    with open(filename, "w") as file:
        file.write(config)

    print(f"Configuration generated for {hostname}")
    print(f"IP Address: {ip}")
    print(f"File: {filename}")