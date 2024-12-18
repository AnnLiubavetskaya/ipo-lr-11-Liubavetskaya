from transport.client import Client
from transport.vehicle import Vehicle

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Аргумент должен быть объектом класса Vehicle.")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return [str(vehicle) for vehicle in self.vehicles]

    def add_client(self, client):
        if not isinstance(client, Client):
            raise ValueError("Аргумент должен быть объектом класса Client.")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        # Сортировауа клиентов vip
        self.clients.sort(key=lambda client: client.is_vip, reverse=True)
        
        # Загружаем грузы в транспортные средства
        for client in self.clients:
            for vehicle in self.vehicles:
                try:
                    vehicle.load_cargo(client)
                    break
                except ValueError:
                    continue