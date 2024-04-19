import socket
import platform

def system_info():
    hostname = socket.gethostname()

    ip_address = socket.gethostbyname(hostname)

    processor_architecture = platform.processor()

    os_version = platform.platform()

    print("Hostname:", hostname)
    print("IP Address:", ip_address)
    print("Processor Architecture:", processor_architecture)
    print("OS Version:", os_version)

system_info()
