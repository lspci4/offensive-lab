# Escaner TCP en python
import sys
import socket


def create_socket(ip,port):
    #print("Creando socket...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        connect_ex = s.connect_ex((ip, port))
        if connect_ex == 0:
            print(f"[+] Host : {ip} and port: {port} is Open")
        else:
            print(f"[-] Host : {ip} and port: {port} Not found...")
        
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
    
    for port in ports:
        create_socket(ip, port)      

if __name__ == "__main__":
    main()