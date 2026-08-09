import socket
import sys

open_ports = []
target = input("Enter target IP or host: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))
    
print(f"\nScanning {target} from port {start_port} to {end_port}...")

def port_scan(target, start_port, end_port):
    try:
        target = socket.gethostbyname(target)
              
    except socket.gaierror:
        print("\n Hostname could not be resolved")
        sys.exit()
    
    except KeyboardInterrupt:
        print("\n Scan halted by user")
        sys.exit()
                    
    except socket.error:
        print("\ Server not responding")
        sys.exit()

    for p in range(start_port, end_port + 1):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, p))
            if result == 0:
                open_ports.append(p)

    print("Open ports:")
    for p in open_ports:
        print(p)

    print("Scan complete")

port_scan(target, start_port, end_port)