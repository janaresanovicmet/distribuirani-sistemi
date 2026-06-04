import asyncio
import os


async def server_pronadji_fajl(naziv_fajla):
    await asyncio.sleep(2)

    if os.path.exists(naziv_fajla):
        return f"Server: fajl '{naziv_fajla}' je pronađen."
    else:
        return f"Server: fajl '{naziv_fajla}' nije pronađen."


async def middleware_pronadji_fajl(naziv_fajla):
    print("Middleware: proveravam fajl sistem...")

    await asyncio.sleep(1)

    odgovor = await server_pronadji_fajl(naziv_fajla)

    return odgovor


async def klijent():
    naziv_fajla = input("Unesite naziv fajla: ")

    zahtev = asyncio.create_task(middleware_pronadji_fajl(naziv_fajla))

    while not zahtev.done():
        print("Klijent nastavlja da radi...")
        await asyncio.sleep(0.5)

    odgovor = await zahtev
    print("Klijent je dobio odgovor:")
    print(odgovor)


asyncio.run(klijent())