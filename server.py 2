import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

# Lock koristimo da više niti ne piše u fajl u istom trenutku
file_lock = threading.Lock()


def handle_client(client_socket, client_address):
    print(f"[NOVA KONEKCIJA] Klijent povezan: {client_address}")

    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")

            if not message:
                break

            if message.lower() == "exit":
                print(f"[KRAJ] Klijent {client_address} je prekinuo konekciju.")
                break

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] {client_address}: {message}"

            print(log_message)

            with file_lock:
                with open("logs.txt", "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")

            client_socket.send("Poruka je uspešno zabeležena.".encode("utf-8"))

    except ConnectionResetError:
        print(f"[GREŠKA] Klijent {client_address} je nasilno prekinuo konekciju.")

    finally:
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER POKRENUT] Server sluša na {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )

        client_thread.start()

        print(f"[AKTIVNE NITI] {threading.active_count() - 1}")


start_server()
