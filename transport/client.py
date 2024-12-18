class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        # Валидация данных
        if not isinstance(name, str) or not name:
            raise ValueError("Имя клиента должно быть строкой и не может быть пустым.")
        if not isinstance(cargo_weight, (int, float)) or cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом.")
        if not isinstance(is_vip, bool):
            raise ValueError("Флаг VIP-статуса должен быть булевым значением.")

        self.name = name
        self.cargo_weight = cargo_weight
        self.is_vip = is_vip