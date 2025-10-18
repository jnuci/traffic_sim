import threading
import socket
import time
import json
from network.client.client import NetworkClient  # update this import if your filename differs

# Dummy server to test receiving JSON
def dummy_server(host, port, message, delay_before_send=0.5):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(1)
    conn, addr = server_sock.accept()
    if delay_before_send:
        time.sleep(delay_before_send)
    conn.sendall(json.dumps(message).encode('utf-8'))
    conn.close()
    server_sock.close()


def test_receive_json():
    host = "127.0.0.1"
    port = 5001  # use a free test port
    test_message = {"status": "ok", "value": 123}

    # Start dummy server in background
    server_thread = threading.Thread(
        target=dummy_server,
        args=(host, port, test_message),
        daemon=True
    )
    server_thread.start()

    # Create NetworkClient and connect
    client = NetworkClient(host, port)
    client.connect()

    # Give the connection a moment
    time.sleep(0.2)

    received = client.receive_JSON()
    print("Test result:", received)


if __name__ == "__main__":
    test_receive_json()