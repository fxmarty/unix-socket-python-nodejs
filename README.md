## unix-socket-python-nodejs

This minimal example illustrates how to communicate between running Python and Node.js processes with a Unix domain socket.

## How to run

1. Clone the repository with `git clone https://github.com/fxmarty/unix-socket-python-nodejs.git`
3. Assuming decently recent versions of Python are installed, run in two terminals, from the repository directory:
- `python socket_server.py` (start the socket server)
- `node socket_client_node.js` (start the socket client)

This minimal example simply sends a message from Python to Node.js, which returns a message back as well as an exit code.

## Expected output

In Python:
```
starting up on ./uds_socket
waiting for a connection
Connection from 
received My answer to you <3
received stop
```

In Node.js:

```
connect
I just want to start a flame in your heart
```
