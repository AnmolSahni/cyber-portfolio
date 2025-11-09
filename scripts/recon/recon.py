#!/usr/bin/env python3
"""recon.py - example recon scaffold"""
import socket, sys
def check_ports(host, ports=(22,80,443)):
    for p in ports:
        try:
            s = socket.create_connection((host, p), timeout=0.5)
            print(f"[+] {p} open")
            s.close()
        except: pass
if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    check_ports(target)
