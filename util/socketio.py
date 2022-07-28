import socketio
from config.config import socket_server
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def message(data):
    print('I received a message!')


sio.connect(url=socket_server)
print('client socket is connected :', sio.connected)
