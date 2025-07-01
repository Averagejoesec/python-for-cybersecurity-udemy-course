# When clients connect they should first send a password that the user on the client types.

# Your server should check to ensure that this password matches.

# If the password does not match then close the connection after sending a message stating 'access denied'

# if the password DOES match, allow that client access to chat with the server like in the example I showed in the lectures with a few additional features.

# When a message is displayed on the client the message should be 'SERVER>>' + msg and vice versa

# If the client sends 'end' to the server, the connection should end

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host and port
host = '127.0.0.1'
port = 9002

# setup to take connections
s.bind((host, port))
s.listen()
conn, addr = s.accept()

print(f"Connection received from {addr}")