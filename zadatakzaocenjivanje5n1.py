import time
import threading


def timeout_middleware(func):
    def wrapper(*args, **kwargs):
        result = [None]

        def target():
            result[0] = func(*args, **kwargs)

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout=2)

        if thread.is_alive():
            return "Vreme čekanja isteklo"

        return result[0]

    return wrapper


@timeout_middleware
def server_request():
    seconds = int(input("Unesite vreme odgovora servera u sekundama: "))
    time.sleep(seconds)
    return "Odgovor servera je uspešno prosleđen klijentu"


response = server_request()
print(response)