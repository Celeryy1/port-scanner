import socket
import sys

open_ports = []
target = input("Provide a target: ")

def port_scan(target):
    for p in range(1, 1023):
        print(f"Scanning target: {target}")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, p))
                if result == 0:
                    open_ports.append(p)
                
        except KeyboardInterrupt:
            print("\n Scan halted by user")
            sys.exit()

        except socket.gaierror:
                print("\n Hostname could not be resolved")
                sys.exit()
                
        except socket.error:
                print("\ Server not responding")
                sys.exit()

    print("Open ports:")
    for p in range(open_ports):
        print(p)


port_scan(target)