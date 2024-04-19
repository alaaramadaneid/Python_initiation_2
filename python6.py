import paramiko

hostname = "192.168.33.10"
port = 22
username = "vagrant"
password = "vagrant"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port=port, username=username, password=password)

commands = [
    "sudo ip addr add 192.168.33.10/24 dev enp0s8",
    "sudo ip link set enp0s8 up",
    "sudo ip route add default via 192.168.33.1"
]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    if output:
        print(output)
    if error:
        print(error)

client.close()
