"""
TCP Port Scanner en Python
Autor: lspci4
Fecha: 2025-05-18
"""
import sys 
import socket
import json

def scan_tcp(ip, ports):
    results = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            output = s.connect_ex((ip, port))
            if output == 0:
                print(f"[+] Host {ip} port {port} status: open")
                results.append({"ip": ip, "port": port, "status": "open"})
            else:
                print(f"[-] Host {ip} y port {port} status: closed")
                results.append({"ip": ip, "port": port, "status": "closed"})
    return results
            
def main():
    if len(sys.argv) != 3:
        print(f"[+] Uso: {sys.argv[0]} <IP> <Port>")
        print(f"[+] Example: {sys.argv[0]} 192.168.1.100 8080 o 8070-8080")
        sys.exit(1)

    if '-' in sys.argv[2]:
        start, end = map(int, sys.argv[2].split('-'))
        ports = range(start, end +1 )
    else:
        ports = int(sys.argv[2])
    
    ip = sys.argv[1]
    print(f"Iniciando scan {ip} y port {ports}")
    
    results = scan_tcp(ip, ports)
    output_json = json.dumps(results, indent=4)
    print("\n Resultdos en JSON:")
    print(output_json)
    
        
        
if __name__ == "__main__":
    main()