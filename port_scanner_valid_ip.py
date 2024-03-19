#!/bin/python3

import sys
import socket
from datetime import datetime
import re

# Function to validate IP address
def validate_ip(ip):
    ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_regex, ip):
        return True
    else:
        return False

# Define our target
if len(sys.argv) == 2:
    if validate_ip(sys.argv[1]):
        target = socket.gethostbyname(sys.argv[1])  # translate hostname to ipv4
    else:
        print("Invalid IP address format.")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 Scanner.py <IP> ")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
    # User input to choose the range of ports
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
