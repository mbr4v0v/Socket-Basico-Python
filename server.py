import socket

def start_server():
    # Define the server address and port
    server_address = 'localhost'
    server_port = 12345

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((server_address, server_port))

    # Listen for incoming connections (max 5 connections)
    server_socket.listen(5)
    print(f"Server listening on {server_address}:{server_port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the data in small chunks and retransmit it
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)  # Echo back the received data

        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
