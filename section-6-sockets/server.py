import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP and host that we want to connect to
host = '127.0.0.1'
port = 9002

s.connect((host, port))

password_rcvd = s.recv(1024).decode()

password = 'password123'
if password_rcvd == password:
    while True:
        data = input("Enter a msg: ")
        s.sendall(str.encode(f"CLEINT>> {data}"))
        msg = s.recv(1024).decode()
        if not msg:
            break
        elif 'end' in msg:
            s.close()
            print('Connection ended.')
            break
        else:
            print(msg)
else:
    s.close()
    print("Incorrect password, connection closed.")