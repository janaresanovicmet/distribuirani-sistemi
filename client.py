import socket

HOST = "127.0.0.1"
PORT = 5000


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    print("Povezani ste na server.")
    print("Unosite poruke. Za kraj unesite: end")

    while True:
        poruka = input("Unesite poruku: ")

        client_socket.send(poruka.encode("utf-8"))

        if poruka.lower() == "end":
            print("Kraj komunikacije.")
            break

        odgovor = client_socket.recv(1024).decode("utf-8")
        print("Server:", odgovor)

    client_socket.close()


start_client()