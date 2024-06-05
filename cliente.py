import socket

def start_client():
    # Define the server address and port
    server_address = 'localhost'
    server_port = 12345

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_address, server_port))
    print(f"Connected to {server_address}:{server_port}")

    try:
        # Send data
        message = "Hello, Server!"
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())

        # Look for the response
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()
