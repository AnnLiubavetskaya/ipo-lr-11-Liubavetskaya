from transport.client import Client
import random
import string

class Vehicle:
    def __init__(self, capacity):
        # Валидация данных
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        
        self.vehicle_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.capacity = capacity
        self.current_load = 0
        self.clients_list = []

    def load_cargo(self, client):
        # Валидация типов данных
        if not isinstance(client, Client):
            raise ValueError("Аргумент должен быть объектом класса Client.")
        if not isinstance(client.cargo_weight, (int, float)) or client.cargo_weight <= 0:
            raise ValueError("Вес груза клиента должен быть положительным числом.")
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Перегрузка! Не хватает места для загрузки груза клиента.")
        
        # Загружаем груз
        self.current_load += client.cargo_weight
        self.clients_list.append(client)

    def __str__(self):
        return f"Транспорт {self.vehicle_id}, грузоподъемность {self.capacity} тонн, текущая загрузка {self.current_load} тонн"