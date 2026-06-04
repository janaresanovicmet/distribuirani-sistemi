class AnalyticsServer:
    def analizaPodataka(self):
        return "Analitika-server je izvršio funkciju analizaPodataka()"


class ReportServer:
    def generisiIzvestaj(self):
        return "Report-server je izvršio funkciju generisiIzvestaj()"


class Broker:
    def __init__(self):
        self.registry = {}

    def register_function(self, function_name, server):
        self.registry[function_name] = server

    def execute_request(self, function_name):
        if function_name not in self.registry:
            return f"Greška: funkcija {function_name} nije pronađena u registru."

        server = self.registry[function_name]

        if not hasattr(server, function_name):
            return f"Greška: server ne može da izvrši funkciju {function_name}."

        function = getattr(server, function_name)
        return function()


class Client:
    def __init__(self, broker):
        self.broker = broker

    def send_request(self, function_name):
        print(f"Klijent šalje zahtev za funkciju: {function_name}")
        response = self.broker.execute_request(function_name)
        print("Odgovor:", response)


analytics_server = AnalyticsServer()
report_server = ReportServer()

broker = Broker()
broker.register_function("analizaPodataka", analytics_server)
broker.register_function("generisiIzvestaj", report_server)

client = Client(broker)

client.send_request("analizaPodataka")