import socket
import os

server_address = './uds_socket'


# Make sure the code will work whether the socket already address already
# exist or not
try:
    os.unlink(server_address)
except OSError as msg:
    if os.path.exists(server_address):
        print('Socket already exists.')
    else:
        print(msg)

# create unix socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('starting up on', server_address)
sock.bind(server_address)

sock.listen(1)

print('waiting for a connection')
connection, client_address = sock.accept()

print('Connection from', client_address)

mydata = 'I just want to start a flame in your heart'
connection.sendall(mydata.encode())


while True:
    # Receive the data in small chunks of 256 characters
    data_received = connection.recv(256)
    
    decoded_data = data_received.decode()
    print(f'received {decoded_data}')
    
    if decoded_data == 'stop':
        break
    
# Clean up the connection
connection.close()