import socket
import json
import time
import select
from model import entity, entityDb

class NetworkClient:

    # socket set to none without context
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.receive_buffer_size = 4096

    def connect(self, delay = 1, attempts = 3):
        # create socket for client to connect on
        # using ipv4 and TCP connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for attempt in range(attempts):
            try:
                self.socket.connect((self.host, self.port))
                print(f"Connected to server on port {self.port}")
                break
            except Exception as e:
                print(f"Attempt {attempt+1} to connect failed: {e}")
                if attempt < attempts-1:
                    time.sleep(delay)            
    
    def is_connected(self):

        if self.socket is None:
            return False
        
        try:
            readable, _, _ = select.select([self.socket], [], [], 0)
            if readable:
                # Try to peek 1 byte without removing it from the buffer
                data = self.socket.recv(1, socket.MSG_PEEK)
                if len(data) == 0:
                    # Connection was closed by the peer
                    return False
            return True
        except BlockingIOError:
            # No data available, but socket is still open
            return True
        except ConnectionResetError:
            # Connection was forcibly closed
            return False
        except OSError:
            # Other socket error (optional)
            return False
    
    def receive_JSON(self):
        if not self.is_connected():
            print("Client not connected")
            return None
        
        # buffer set in constructor
        response = self.socket.recv(self.receive_buffer_size)
        if response:
            try:
                data = json.loads(response.decode('utf-8'))
                print("received JSON data")
                print(data)
                return data
            except:
                print("Invalid JSON response", response.decode('utf-8'))
                return None
            
        return None
    
    def send_command(self):
        if not self.is_connected():
            print("Client not connected")
            return None
        
        try:
            message = json.dumps({"command": "Hello from python client!"}) + '\n'
            self.socket.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"Exception occurred: {e}")




## end NetworkClient
