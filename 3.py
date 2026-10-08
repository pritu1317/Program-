from xmlrpc.server import SimpleXMLRPCServer

messages = []

def send_message(name, msg):
    messages.append(f"{name}: {msg}")
    return "Message sent!"

def get_messages():
    return messages

server = SimpleXMLRPCServer(("127.0.0.1", 8000), allow_none=True)

server.register_function(send_message)
server.register_function(get_messages)

print("RPC Chat Server Started...")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer Stopped")

/////////

import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")
print(client.send_message("MCA 2026", "div E"))
print(client.send_message("hello", "BCA Students"))

print("\nChat Messages:")
for msg in client.get_messages():
    print(msg)
    



