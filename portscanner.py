import socket
import sys
from datetime import datetime

open_ports = []
target = input("Enter target IP or host: ")

def validate_target(target):
    try:
         target = socket.gethostbyname(target)
         return target
    
    except socket.gaierror:
        print("\nHostname could not be resolved")
        sys.exit()

    except KeyboardInterrupt:
        print("\nScan halted by user")
        sys.exit()

    except socket.error:
        print("\nServer not responding")
        sys.exit()

def port_scan(target):

    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    for p in range(1, 65536):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, p))

            if result == 0:
                open_ports.append(p)

    print("Open ports:")
    for p in open_ports:
        print(p)

    print("Scan complete")

validated_target = validate_target(target)
port_scan(validated_target)
