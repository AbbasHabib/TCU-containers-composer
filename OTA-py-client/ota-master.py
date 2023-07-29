import socket
import subprocess

# Define server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12349

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming messages

output = subprocess.check_output("echo 'P@ssw0rd123' | docker login vehicleplus.cloud --username PI --password-stdin", shell=True)

print('UDP server listening on {}:{}'.format(SERVER_IP, SERVER_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(message)
    command = ""
    if message == "yes":
        command = "cd /etc/compose_files/new ; docker-compose up -d; cp -f /etc/compose_files/new/docker-compose.yaml /etc/compose_files/old/docker-compose.yaml"
    elif message == "no":
        command = "cd /etc/compose_files/old ; docker-compose up"
    print(command)
    output = subprocess.check_output(command, shell=True)

    break

