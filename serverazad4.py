import socket
import os
import time

SERVER_B_HOST = "127.0.0.1"
SERVER_B_PORT = 5001
DATA_FILE = "data.txt"


def get_local_file_size():
    if os.path.exists(DATA_FILE):
        return os.path.getsize(DATA_FILE)
    return 0


def send_request_to_server_b(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_B_HOST, SERVER_B_PORT))
    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    client_socket.close()

    return response


def start_server_a():
    print("Server A pokrenut.")

    while True:
        local_size = get_local_file_size()
        remote_size = int(send_request_to_server_b("GET_SIZE"))

        print(f"Lokalna veličina: {local_size}")
        print(f"Veličina na Serveru B: {remote_size}")

        if local_size != remote_size:
            message = f"DIFFERENCE: Server A data.txt = {local_size}, Server B data.txt = {remote_size}"
            response = send_request_to_server_b(message)
            print("Server B:", response)
        else:
            print("Datoteke su iste veličine.")

        time.sleep(10)


start_server_a()