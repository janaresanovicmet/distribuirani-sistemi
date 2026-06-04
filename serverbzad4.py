import socket
import os
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5001
DATA_FILE = "data.txt"
LOG_FILE = "replication.log"


def get_file_size():
    if os.path.exists(DATA_FILE):
        return os.path.getsize(DATA_FILE)
    return 0


def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time_now}] {message}\n")


def start_server_b():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server B pokrenut na {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode("utf-8")

        if request == "GET_SIZE":
            size = get_file_size()
            client_socket.send(str(size).encode("utf-8"))

        elif request.startswith("DIFFERENCE"):
            write_log(request)
            client_socket.send("LOGGED".encode("utf-8"))

        client_socket.close()


start_server_b()