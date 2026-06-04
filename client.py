import socket

HOST = "127.0.0.1"
PORT = 5000


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    print("Povezani ste na server.")
    print("Unesite log poruke. Za kraj unesite 'exit'.")

    while True:
        message = input("Log poruka: ")

        client_socket.send(message.encode("utf-8"))

        if message.lower() == "exit":
            break

        response = client_socket.recv(1024).decode("utf-8")
        print("Server:", response)

    client_socket.close()


start_client()