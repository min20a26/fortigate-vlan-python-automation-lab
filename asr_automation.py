

import subprocess

command = [
    "ssh",
    "-o", "KexAlgorithms=+diffie-hellman-group14-sha1",
    "-o", "HostKeyAlgorithms=+ssh-rsa",
    "admin@192.168.30.110",
    "show ip interface brief"

    ]
output = subprocess.run(command, capture_output=True, text=True)

print(output.stdout)

with open("show_ip_interface_brief.txt", "w") as file:

    file.write(output.stdout)
