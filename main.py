from servera import ServerA
from serverb import ServerB


class CentralniImenik:
    def __init__(self):
        self.registar = {
            "A": ServerA(),
            "B": ServerB()
        }

    def pronadji_server(self, izbor_modula):
        return self.registar.get(izbor_modula)


class Middleware:
    def __init__(self, imenik):
        self.imenik = imenik

    def prosledi_zahtev(self, izbor_modula, funkcija, podaci):
        server = self.imenik.pronadji_server(izbor_modula)

        if server is None:
            return "Greška: izabrani modul ne postoji."

        if not hasattr(server, funkcija):
            return "Greška: funkcija ne postoji na izabranom serveru."

        metoda = getattr(server, funkcija)
        return metoda(podaci)


class Klijent:
    def __init__(self, middleware):
        self.middleware = middleware

    def posalji_zahtev(self):
        print("Izaberite modul:")
        print("A - Modul A / Server A")
        print("B - Modul B / Server B")

        izbor = input("Unesite izbor: ").upper()
        podaci = input("Unesite podatke za obradu: ")

        odgovor = self.middleware.prosledi_zahtev(
            izbor,
            "obradi_podatke",
            podaci
        )

        print("Odgovor:", odgovor)


imenik = CentralniImenik()
middleware = Middleware(imenik)
klijent = Klijent(middleware)

klijent.posalji_zahtev()