from transport.vehicle import Vehicle

class Airplane(Vehicle):
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity)
        if not isinstance(max_altitude, (int, float)) or max_altitude <= 0:
            raise ValueError("Максимальная высота полета должна быть положительным числом.") #Валидация
        self.max_altitude = max_altitude

    def get_load_percentage(self):
        return (self.current_load / self.capacity) * 100

    def __str__(self):
        return f"Самолет {self.vehicle_id}, грузоподъемность {self.capacity} тонн, максимальная высота {self.max_altitude} метров, текущая загрузка {self.current_load} тонн"
