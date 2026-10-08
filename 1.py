import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def handle_client(client_socket, address):
    print("Client connected:", address)

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode()
        print("Client:", message)

        client_socket.send(data)

    client_socket.close()
    print("Client disconnected:", address)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(5)

print("Echo Server started...")
print("Waiting for clients...")

while True:
    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    thread.start()


    import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to Echo Server")
print("Type 'exit' to close")

while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

    response = client.recv(1024).decode()

    print("Server Echo:", response)

client.close()