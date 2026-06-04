import socket

HOST = "127.0.0.1"
PORT = 5000


def obrni_redosled_reci(poruka):
    reci = poruka.split(" ")
    reci.reverse()
    return " ".join(reci)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server je pokrenut na {HOST}:{PORT}")
    print("Čekam klijenta...")

    client_socket, client_address = server_socket.accept()
    print(f"Klijent se povezao: {client_address}")

    while True:
        poruka = client_socket.recv(1024).decode("utf-8")

        if not poruka:
            break

        print("Klijent:", poruka)

        with open("client_log.txt", "a", encoding="utf-8") as file:
            file.write(poruka + "\n")

        if poruka.lower() == "end":
            print("Klijent je poslao end. Završavam server.")
            break

        odgovor = obrni_redosled_reci(poruka)

        client_socket.send(odgovor.encode("utf-8"))

    client_socket.close()
    server_socket.close()


start_server()