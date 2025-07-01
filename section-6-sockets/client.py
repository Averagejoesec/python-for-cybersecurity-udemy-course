import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host and port
host = '127.0.0.1'
port = 9002

# setup to take connections
s.bind((host, port))
s.listen()
client, addr = s.accept()

print(f"Connection received from {addr}")

password = input("Password: ")
client.sendall(str.encode(password))

while True:
        data = input("Enter a msg: ")
        client.sendall(str.encode(f"SERVER>> {data}"))
        msg = client.recv(1024).decode()
        if not msg:
            break
        elif 'end' in msg:
            client.close()
            print("Connection ended.")
            break
        else:
            print(msg)

client.close()
print(f"Connection {addr} has been closed")