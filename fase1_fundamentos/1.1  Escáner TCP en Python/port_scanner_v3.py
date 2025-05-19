# Escaner TCP en python
import sys
import socket
import json


def create_socket(ip,ports):
    results = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            connect_ex = s.connect_ex((ip, port))
            if connect_ex == 0:
                print(f"[+] Host : {ip} and port: {port} is Open")
                results.append({"ip": ip, "port": port, "status": "open"})
            else:
                print(f"[-] Host : {ip} and port: {port} Not found...")
                results.append({"ip": ip, "port": port, "status": "closed"})       
    return results 
            
def main():
    if len(sys.argv) != 3:
        print(f"[+] Uso: {sys.argv[0]} <IP> <PORT>")
        print(f"[+] Example: {sys.argv[0]} 192.168.1.100 8080")
        sys.exit(1)
    
    
    ip = sys.argv[1]
    
    if '-' in sys.argv[2]:
        start, end = map(int, sys.argv[2].split('-'))
        ports = range(start, end + 1)
    else:
        ports = [int(sys.argv[2])]
        
    print(f" Escaneando {ip} en puertos: {ports}")  
    
    results = create_socket(ip, ports)
        
    output_json = json.dumps(results, indent=4)
    print("\n Resultados en JSON:")
    print(output_json)

if __name__ == "__main__":
    main()