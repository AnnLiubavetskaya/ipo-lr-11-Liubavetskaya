from transport.vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated=False):
        super().__init__(capacity) #Наследование 
        if not isinstance(is_refrigerated, bool):
            raise ValueError("Флаг холодильника должен быть булевым значением.")
        self.is_refrigerated = is_refrigerated

    def __str__(self):
        return f"Фургон {self.vehicle_id}, грузоподъемность {self.capacity} тонн, холодильник: {self.is_refrigerated}, текущая загрузка {self.current_load} тонн"
    
    def get_load_percentage(self):
        return (self.current_load / self.capacity) * 100
