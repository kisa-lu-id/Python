#TCP_server.py

import socket
from datetime import datetime

def start_server():
    #AF_INET = IPv4, SOCK_STREAM = TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #assign to port 50010
    server_address = ('0.0.0.0', 50010)
    server_socket.bind(server_address)
    
    server_socket.listen(1)
    print(f"Server wartet auf Nachricht (Port 50010)...")
    
    connection, address_client = server_socket.accept()
    
    with connection:
        while True:
            #listen, buffer size 1024
            data = connection.recv(1024)
            if not data:
                #print(f"data is empty")
                continue
                
            message = data.decode('utf-8').strip()
            
            if not message: #skip empty lines
                continue
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if message.upper() == "QUIT":
                print(f"[{timestamp}] Client {address_client} hat die Verbindung beendet.")
                break
            
            if message.upper() == "HEARTBEAT_SIGNAL":
                print(f"[{timestamp}] Signal empfangen: {message}")
                

            else:
                 print(f"[{timestamp}] Empfangen von {address_client}: \n{message}")
            
            #report to the client
            response = f"Server hat die Nachricht bekommen: {message}"
            connection.sendall(response.encode("utf-8"))
    
    server_socket.close()


if __name__ == "__main__":
    start_server()
